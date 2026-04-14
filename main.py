import json
from pathlib import Path

from langchain_groq import ChatGroq

from chains.intent_chain import (
	build_extraction_chain,
	build_matching_chain,
	run_extraction,
	run_matching,
)
from chains.response_chain import (
	build_explanation_chain,
	build_scoring_chain,
	run_explanation,
	run_scoring,
)
from utlis.config import load_config, validate_required_config


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"


def read_text_file(file_path: Path) -> str:
	return file_path.read_text(encoding="utf-8").strip()


def extract_candidate_name(resume_text: str) -> str:
	"""Extract candidate name from resume text."""
	lines = resume_text.split('\n')
	for line in lines:
		if line.startswith('Name:'):
			return line.replace('Name:', '').strip()
	return "Unknown Candidate"


def load_sample_inputs() -> tuple[str, dict[str, str]]:
	job_description = read_text_file(
		DATA_DIR / "job_descriptions" / "data_scientist_jd.txt"
	)
	resumes = {
		"Ananya Sharma": read_text_file(DATA_DIR / "resumes" / "Ananya_Sharma.txt"),
		"Priya Patel": read_text_file(
			DATA_DIR / "resumes" / "Priya_Patel.txt"
		),
		"Rajesh Singh": read_text_file(DATA_DIR / "resumes" / "Rajesh_Singh.txt"),
	}
	return job_description, resumes


def detect_potential_hallucinations(extracted_profile: dict, resume_text: str) -> list[str]:
	resume_lower = resume_text.lower()
	flagged_items = []

	for key in ["skills", "tools", "certifications"]:
		for item in extracted_profile.get(key, []):
			if isinstance(item, str) and item.lower() not in resume_lower:
				flagged_items.append(f"{key}:{item}")

	return flagged_items


def run_pipeline_for_candidate(
	candidate_name: str,
	resume_text: str,
	job_description: str,
	extraction_chain,
	matching_chain,
	scoring_chain,
	explanation_chain,
	run_tags: list[str],
) -> dict:
	extracted_profile = run_extraction(
		extraction_chain,
		resume_text,
		tags=run_tags + ["step:extract"],
	)
	match_analysis = run_matching(
		matching_chain,
		job_description,
		extracted_profile,
		tags=run_tags + ["step:match"],
	)
	score_json = run_scoring(
		scoring_chain,
		job_description,
		extracted_profile,
		match_analysis,
		tags=run_tags + ["step:score"],
	)
	explanation_json = run_explanation(
		explanation_chain,
		candidate_name,
		score_json,
		extracted_profile,
		match_analysis,
		tags=run_tags + ["step:explain"],
	)

	debug_flags = detect_potential_hallucinations(extracted_profile, resume_text)

	return {
		"candidate_name": candidate_name,
		"extracted_profile": extracted_profile,
		"match_analysis": match_analysis,
		"score": score_json,
		"explanation": explanation_json,
		"debug_flags": debug_flags,
	}


def print_summary(result: dict) -> None:
	print("=" * 88)
	print(f"Candidate: {result['candidate_name']}")
	print(f"Fit Score: {result['score'].get('fit_score', 'N/A')}")
	print(f"Decision: {result['explanation'].get('decision', 'N/A')}")

	if result["debug_flags"]:
		print("Potential debug issue (hallucination risk):")
		for flag in result["debug_flags"]:
			print(f"  - {flag}")

	print("Top reasons:")
	for reason in result["explanation"].get("why_this_score", [])[:3]:
		print(f"  - {reason}")


def main() -> None:
	config = load_config()
	validate_required_config(config)

	llm = ChatGroq(model=config.groq_model, temperature=0)

	extraction_chain = build_extraction_chain(llm)
	matching_chain = build_matching_chain(llm)
	scoring_chain = build_scoring_chain(llm)
	explanation_chain = build_explanation_chain(llm)

	job_description, resumes = load_sample_inputs()

	all_results = []

	for candidate_name, resume_text in resumes.items():
		result = run_pipeline_for_candidate(
			candidate_name=candidate_name,
			resume_text=resume_text,
			job_description=job_description,
			extraction_chain=extraction_chain,
			matching_chain=matching_chain,
			scoring_chain=scoring_chain,
			explanation_chain=explanation_chain,
			run_tags=["assignment", "baseline", candidate_name],
		)
		all_results.append(result)
		print_summary(result)

	debug_case = run_pipeline_for_candidate(
		candidate_name="Ananya Sharma (Debug Run)",
		resume_text=resumes["Ananya Sharma"],
		job_description=job_description,
		extraction_chain=extraction_chain,
		matching_chain=matching_chain,
		scoring_chain=scoring_chain,
		explanation_chain=explanation_chain,
		run_tags=["assignment", "debug", "incorrect-output-simulation"],
	)
	print_summary(debug_case)

	output_path = BASE_DIR / "screening_results.json"
	output_payload = {"runs": all_results + [debug_case]}
	output_path.write_text(json.dumps(output_payload, indent=2), encoding="utf-8")

	print("=" * 88)
	print(f"Saved all results to: {output_path}")
	print("Check LangSmith traces for step-level runs and debug tags.")


if __name__ == "__main__":
	main()
