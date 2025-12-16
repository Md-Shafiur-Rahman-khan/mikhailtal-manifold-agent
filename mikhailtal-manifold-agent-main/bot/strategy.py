def estimate_true_probability(market_probability: float) -> float:
    """
    Conservative probability shrinkage.
    Improves calibration and reduces overconfidence.
    """
    return 0.7 * market_probability + 0.3 * 0.5


def llm_probability_estimate(question: str, description: str) -> float:
    """
    Optional LLM-based probability estimate.
    Replace stub with OpenAI / Perplexity / local model.
    """
    return 0.55


def final_probability(market_p: float, use_llm: bool = False,
                      question: str = "", description: str = "") -> float:
    if not use_llm:
        return estimate_true_probability(market_p)

    llm_p = llm_probability_estimate(question, description)
    return 0.6 * market_p + 0.4 * llm_p

