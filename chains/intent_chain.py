from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

from prompts.intent_prompt import get_matching_prompt, get_skill_extraction_prompt


def build_extraction_chain(llm: ChatOpenAI):
	parser = JsonOutputParser()
	return get_skill_extraction_prompt() | llm | parser


def build_matching_chain(llm: ChatOpenAI):
	parser = JsonOutputParser()
	return get_matching_prompt() | llm | parser


def run_extraction(extraction_chain, resume_text: str, tags: list[str] | None = None):
	return extraction_chain.invoke(
		{"resume_text": resume_text},
		config={"tags": tags or ["skill-extraction", "resume-screening"]},
	)


def run_matching(
	matching_chain,
	job_description: str,
	extracted_profile: dict,
	tags: list[str] | None = None,
):
	return matching_chain.invoke(
		{
			"job_description": job_description,
			"extracted_profile": extracted_profile,
		},
		config={"tags": tags or ["matching-logic", "resume-screening"]},
	)
