from src.document_loader import load_document, split_into_sections
from src.hybrid_search import hybrid_search


# Define test questions and expected sections

test_cases = [
    {
        "question": "Who authorizes major expenditures for artificial intelligence projects?",
        "expected_section": "SECTION 2"
    },
    {
        "question": "What security review is required before deploying AI?",
        "expected_section": "SECTION 3"
    },
    {
        "question": "What information must an AI business case contain?",
        "expected_section": "SECTION 4"
    },
    {
        "question": "What is the purpose of the corporate AI investment policy?",
        "expected_section": "SECTION 1"
    }
]


def evaluate_retrieval():

    document = load_document("ai_investment_policy.txt")
    chunks = split_into_sections(document)

    successful = 0

    for test in test_cases:

        results = hybrid_search(
            test["question"],
            chunks,
            top_k=3
        )

        retrieved_text = "\n".join(
            result["content"] for result in results
        )

        found = test["expected_section"] in retrieved_text

        if found:
            successful += 1

        print(f"\nQuestion: {test['question']}")
        print(f"Expected: {test['expected_section']}")
        print(f"Found in top 3: {found}")

    recall_at_3 = successful / len(test_cases)

    print("\nRETRIEVAL EVALUATION")
    print("--------------------")
    print(f"Questions evaluated: {len(test_cases)}")
    print(f"Successful retrievals: {successful}")
    print(f"Hit rate @3: {recall_at_3:.1%}")


if __name__ == "__main__":
    evaluate_retrieval()
