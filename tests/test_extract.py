# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
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
import json
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from neon_utterance_pronomial_plugin import *


class PronomialTransformerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.extractor = PronomialTransformer()

    def test_transform(self):
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
        answer=[['My neighbors have a cat . cat has a bushy tail .', 'My neighbors have a cat. It has a bushy tail.'],
['Here is the book now take book .', 'Here is the book now take it.'],
['The sign was too far away for the boy to read sign .', 'The sign was too far away for the boy to read it.'],
["Dog is man ' s best friend . Dog is always loyal .", "Dog is man's best friend. It is always loyal."],
['The girl said girl would take the trash out .', 'The girl said she would take the trash out.'],
['I voted for Nader because Nader is clear about Nader values . Nader ideas represent a majority of the nation . Nader is better than Rajeev .', 'I voted for Nader because he is clear about his values. His ideas represent a majority of the nation. He is better than Rajeev.'],
["Jack von Doom is one of the top candidates in the elections . Doom ideas are unique compared to Neha ' s .", "Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Neha's."],
['Members voted for John because Members see John as a good leader .', 'Members voted for John because they see him as a good leader.'],
['Leaders around the world say Leaders stand for peace .', 'Leaders around the world say they stand for peace.'],
['My neighbours just adopted a puppy . neighbours care for puppy like a baby .', 'My neighbours just adopted a puppy. They care for it like a baby.'],
['I have many friends . friends are an important part of my life .', 'I have many friends. They are an important part of my life.'],
['Jarbas has a dog named Jurebes . Jarbas loves Jarbas dog !', 'Jarbas has a dog named Jurebes. He loves his dog!'],
['London is the capital and most populous city of England and the United Kingdom . Standing on the River Thames in the south east of the island of Great Britain , London has been a major settlement for two millennia . London was founded by the Romans , Romans named London Londinium .', 'London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium.']
]
        i=0
        for utt in test:
            lang=PronomialTransformer().transform([utt])[0]
            self.assertEqual(lang, (answer[i]))
            i+=1
            #lang = self.extractor.transform([test])
            print(lang)
