from collections import namedtuple
import random

from models import Sentence

fint_card = namedtuple('fint_card',
                       ["sentence_text_original", "sentence_text_translate", "sentence_id", "sentence_category",
                        'translate_state'])


def weighted_random_choice(choices):
    """Randomly select a value from a list of tuples with a probability weight for each choice."""
    total_weight = sum(weight for value, weight in choices)
    rand_weight = random.uniform(0, total_weight)
    for value, weight in choices:
        if rand_weight < weight:
            return value
        rand_weight -= weight
    # Shouldn't get here, but just in case, return the last choice
    return value


# TEST 10000 variables 0.7
# async def generate_card_pool(sentences: list[Sentence], translate_state: bool) -> list[dict]:
#     choice_category = [(0, 0.1), (1, 0.30), (2, 0.6)]  # 0 - remember, 1 - not remember, 2 - not see
#     result = list()
#     not_in_pool = list()
#     while len(sentences) >= 1:
#         category_not_in_pool = True
#         category = weighted_random_choice(choice_category)
#         if category not in not_in_pool:
#             for i in range(len(sentences)):
#                 if sentences[i].category_remember == category:
#                     result.append({
#                         "sentence_text_original": sentences[i].text_original,
#                         "sentence_text_translate": sentences[i].text_translate,
#                         "sentence_id": sentences[i].id,
#                         "sentence_category": sentences[i].category_remember,
#                         "translate_state": translate_state})
#                     del sentences[i]
#                     category_not_in_pool = False
#                     break
#             if category_not_in_pool:
#                 not_in_pool.append(category)
#     return result
async def generate_card_pool(sentences: list[Sentence], translate_state: bool = False) -> list[dict]:
    result = list()

    for sentence in sentences:
        translate_state = True if sentence.category_remember == 0 else False
        result.append({
            "sentence_text_original": sentence.text_original,
            "sentence_text_translate": sentence.text_translate,
            "sentence_id": sentence.id,
            "sentence_category": sentence.category_remember,
            "translate_state": translate_state})

    return result
