import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class AppConfig:
    groq_api_key: str
    groq_model: str
    langchain_tracing_v2: str
    langchain_api_key: str
    langchain_project: str


def load_config() -> AppConfig:
    load_dotenv()

    return AppConfig(
        groq_api_key=os.getenv("GROQ_API_KEY", ""),
        groq_model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        langchain_tracing_v2=os.getenv("LANGCHAIN_TRACING_V2", "true"),
        langchain_api_key=os.getenv("LANGCHAIN_API_KEY", ""),
        langchain_project=os.getenv("LANGCHAIN_PROJECT", "resume-screening-system"),
    )


def validate_required_config(config: AppConfig) -> None:
    if not config.groq_api_key:
        raise ValueError(
            "Missing GROQ_API_KEY. Add it to your environment or `.env` file before running."
        )