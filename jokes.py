import random
import win32com.client


def speak(audiostring):
    print(audiostring)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audiostring)


def telljoke():
    x = str(random.randint(1,10))

    joke = {
    '1':'Girl: You would be a good dancer except for two things. Boy: What are the two things? Girl: Your feet.',
    '2':'A family of mice were surprised by a big cat. Father Mouse jumped and and said, "Bow-wow!" The cat ran away. "What was that, Father?" asked Baby Mouse. "Well, son, thats why it is important to learn a second language."',
    '3':'My friend said he knew a man with a wooden leg named Smith. So I asked him "What was the name of his other leg?" ',
    '4':'The doctor to the patient: "You are very sick". The patient to the doctor: "Can I get a second opinion?" The doctor again: "Yes, you are very ugly too..." ',
    '5':' Patient: Doctor, I have a pain in my eye whenever I drink tea. Doctor: Take the spoon out of the mug before you drink. ',
    '6':"Patient: Doctor! You've got to help me! Nobody ever listens to me. No one ever pays any attention to what I have to say. Doctor: Next please! ",
    '7':"A: Hey, man! Please call me a taxi. Yes, sir. You are a taxi. ",
    '8':"Son: Dad, what is an idiot? Dad: An idiot is a person who tries to explain his ideas in such a strange and long way that another person who is listening to him can't understand him. Do you understand me? Son: No.",
    '9':"Girl: Why do you take baths in milk? Boy: I cant find a cow tall enough for a shower. ",
    '10':"Boy: I was born in California. Girl: Which part? Boy: All of me."
    }
    speak(joke[x])
    return