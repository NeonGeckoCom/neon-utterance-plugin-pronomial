# # NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# # All trademark and other rights reserved by their respective owners
# # Copyright 2008-2021 Neongecko.com Inc.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from neon_transformers import UtteranceTransformer
import pronomial
from neon_transformers.tasks import UtteranceTask


class PronomialTransformer(UtteranceTransformer):
    task = UtteranceTask.COREFERENCE_RESOLUTION

    def __init__(self, name="pronomial", priority=70):
        super().__init__(name, priority)

    def transform(self, utterances, context=None):
        context = context or {}
        lang = context.get("lang", "en-us")
        # replace coreferences
        solved = [pronomial.replace_corefs(utt, lang) for utt in utterances]
        solved = [u for u in solved if u not in utterances]
        # return augmented utterances
        return solved + utterances, {}

test = [
    "My neighbors have a cat. It has a bushy tail.",
    "Here is the book now take it.",
    "The sign was too far away for the boy to read it.",
    "Dog is man's best friend. It is always loyal.",
    "The girl said she would take the trash out.",
    "I voted for Nader because he is clear about his values. His ideas represent a majority of the nation. He is better than Rajeev.",
    "Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Neha's.",
    "Members voted for John because they see him as a good leader.",
    "Leaders around the world say they stand for peace.",
    "My neighbours just adopted a puppy. They care for it like a baby.",
    "I have many friends. They are an important part of my life.",
    "Jarbas has a dog named Jurebes. He loves his dog!",
    "London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium."
]
for utt in test:
    print(PronomialTransformer().transform([utt])[0])