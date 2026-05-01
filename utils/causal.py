from dowhy import CausalModel

def run_causal_analysis(df, cause, effect):
    model = CausalModel(
        data=df,
        treatment=cause,
        outcome=effect,
        common_causes=None
    )

    identified_model = model.identify_effect()
    estimate = model.estimate_effect(
        identified_model,
        method_name="backdoor.linear_regression"
    )

    summary = f"Estimated causal effect of {cause} on {effect}: {round(estimate.value, 3)}"

    return {
        "summary": summary,
        "details": str(estimate)
    }
