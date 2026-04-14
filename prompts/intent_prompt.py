from langchain_core.prompts import PromptTemplate


def get_skill_extraction_prompt() -> PromptTemplate:
	template = """
You are an accurate resume information extractor.

TASK:
Extract candidate information from the resume text.

RULES:
1) Use only evidence present in the resume.
2) Do NOT assume or infer missing skills.
3) If information is missing, return an empty list or null.
4) Keep extracted items concise and normalized.

OUTPUT FORMAT:
Return valid JSON only with this schema:
{{
  "skills": ["..."],
  "tools": ["..."],
  "experience_summary": "...",
  "experience_years": <number or null>,
  "education": "...",
  "certifications": ["..."],
  "projects_domains": ["..."],
  "evidence": ["short quotes from resume"]
}}

Few-shot guidance:
- Resume says "Built ML model using scikit-learn and pandas" -> include "Machine Learning", "scikit-learn", "pandas".
- Resume does not mention "AWS" -> do not add "AWS".

Resume Text:
{resume_text}
"""
	return PromptTemplate(input_variables=["resume_text"], template=template)


def get_matching_prompt() -> PromptTemplate:
	template = """
You are a strict resume-job matcher.

Compare extracted candidate profile against the job description.

RULES:
1) Match only explicit evidence.
2) No hallucinated assumptions.
3) Separate matched, partially matched, and missing requirements.

OUTPUT FORMAT:
Return valid JSON only:
{{
  "matched_requirements": ["..."],
  "partial_matches": ["..."],
  "missing_requirements": ["..."],
  "match_rationale": ["..."]
}}

Job Description:
{job_description}

Extracted Candidate Profile (JSON):
{extracted_profile}
"""
	return PromptTemplate(
		input_variables=["job_description", "extracted_profile"],
		template=template,
	)
