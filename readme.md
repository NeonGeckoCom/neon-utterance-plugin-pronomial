```python
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
```

output
```python
['My neighbors have a cat. It has a bushy tail.', 'My neighbors have a cat . cat has a bushy tail .']
['Here is the book now take it.', 'Here is the book now take book .']
['The sign was too far away for the boy to read it.', 'The sign was too far away for the boy to read sign .']
["Dog is man's best friend. It is always loyal.", "Dog is man ' s best friend . Dog is always loyal ."]
['The girl said she would take the trash out.', 'The girl said girl would take the trash out .']
['I voted for Nader because he is clear about his values. His ideas represent a majority of the nation. He is better than Rajeev.', 'I voted for Nader because Nader is clear about Nader values . Nader ideas represent a majority of the nation . Nader is better than Rajeev .']
["Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Neha's.", "Jack von Doom is one of the top candidates in the elections . Doom ideas are unique compared to Neha ' s ."]
['Members voted for John because they see him as a good leader.', 'Members voted for John because Members see John as a good leader .']
['Leaders around the world say they stand for peace.', 'Leaders around the world say Leaders stand for peace .']
['My neighbours just adopted a puppy. They care for it like a baby.', 'My neighbours just adopted a puppy . neighbours care for puppy like a baby .']
['I have many friends. They are an important part of my life.', 'I have many friends . friends are an important part of my life .']
['Jarbas has a dog named Jurebes. He loves his dog!', 'Jarbas has a dog named Jurebes . Jarbas loves Jarbas dog !']
['London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium.', 'London is the capital and most populous city of England and the United Kingdom . Standing on the River Thames in the south east of the island of Great Britain , London has been a major settlement for two millennia . London was founded by the Romans , Romans named London Londinium .']
```