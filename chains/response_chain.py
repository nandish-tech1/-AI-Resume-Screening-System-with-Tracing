from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

from prompts.response_prompt import get_explanation_prompt, get_scoring_prompt


def build_scoring_chain(llm: ChatOpenAI):
	parser = JsonOutputParser()
	return get_scoring_prompt() | llm | parser


def build_explanation_chain(llm: ChatOpenAI):
	parser = JsonOutputParser()
	return get_explanation_prompt() | llm | parser


def run_scoring(
	scoring_chain,
	job_description: str,
	extracted_profile: dict,
	match_analysis: dict,
	tags: list[str] | None = None,
):
	return scoring_chain.invoke(
		{
			"job_description": job_description,
			"extracted_profile": extracted_profile,
			"match_analysis": match_analysis,
		},
		config={"tags": tags or ["scoring", "resume-screening"]},
	)


def run_explanation(
	explanation_chain,
	candidate_name: str,
	score_json: dict,
	extracted_profile: dict,
	match_analysis: dict,
	tags: list[str] | None = None,
):
	return explanation_chain.invoke(
		{
			"candidate_name": candidate_name,
			"score_json": score_json,
			"extracted_profile": extracted_profile,
			"match_analysis": match_analysis,
		},
		config={"tags": tags or ["explanation", "resume-screening"]},
	)
