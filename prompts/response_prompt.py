from langchain_core.prompts import PromptTemplate


def get_scoring_prompt() -> PromptTemplate:
		template = """
You are a resume screening scoring engine.

Score candidate fit from 0 to 100 based on:
- Skills and tools alignment (40%)
- Relevant experience (30%)
- Domain/project relevance (20%)
- Education/certifications relevance (10%)

RULES:
1) Use only provided data.
2) No assumptions.
3) Keep score as integer between 0 and 100.

OUTPUT FORMAT:
Return valid JSON only:
{{
	"fit_score": <integer 0-100>,
	"score_breakdown": {{
		"skills_tools": <0-40>,
		"experience": <0-30>,
		"domain_relevance": <0-20>,
		"education_certifications": <0-10>
	}},
	"risk_flags": ["..."]
}}

Job Description:
{job_description}

Extracted Candidate Profile (JSON):
{extracted_profile}

Match Analysis (JSON):
{match_analysis}
"""
		return PromptTemplate(
				input_variables=["job_description", "extracted_profile", "match_analysis"],
				template=template,
		)


def get_explanation_prompt() -> PromptTemplate:
		template = """
You are an explainable AI assistant for recruiters.

Generate a concise, recruiter-friendly explanation for the final score.

RULES:
1) Refer to evidence from extracted profile and match analysis.
2) Mention strengths and gaps.
3) Avoid assumptions beyond the data.

OUTPUT FORMAT:
Return valid JSON only:
{{
	"decision": "Strong Fit | Moderate Fit | Low Fit",
	"why_this_score": ["...", "...", "..."],
	"improvement_suggestions": ["...", "..."]
}}

Candidate Name: {candidate_name}
Fit Score JSON:
{score_json}

Extracted Candidate Profile (JSON):
{extracted_profile}

Match Analysis (JSON):
{match_analysis}
"""
		return PromptTemplate(
				input_variables=["candidate_name", "score_json", "extracted_profile", "match_analysis"],
				template=template,
		)
