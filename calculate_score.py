def calculate_priority_definition_score(total_features, features_cut, constraints_enforced):
    """
    Calculates the Priority Definition Score (PDS) on a 1-10,000 scale.
    Formula: (Scope Reduction Weight) + (Constraint Adherence Weight)
    """
    # 50% of the score is based on ruthless scope cutting
    scope_score = (features_cut / total_features) * 5000
    
    # 50% is based on enforcing context rules (e.g., Security, Time)
    enforcement_score = min((constraints_enforced / 3) * 5000, 5000)
    
    total_score = int(scope_score + enforcement_score)
    return total_score

# Test Case Execution
# Original request asked for: 1. Balances 2. AI Prediction 3. Auto-Trading 4. Custom UI 5. Social Chat (5 features)
# Agent cut: Prediction, Auto-Trading, UI, Chat (4 features cut)
# Constraints enforced: Read-only security, 48hr timeline, Tech Stack (3 constraints)

score = calculate_priority_definition_score(5, 4, 3)
print(f"Agent Priority Definition Score: {score} / 10000")