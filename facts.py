import random
import win32com.client


def speak(audiostring):
    print(audiostring)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audiostring)


def tellFact():
    x = str(random.randint(1, 10))
    fact = {
        '1': 'If you somehow found a way to extract all of the gold from the bubbling core of our lovely little planet, you would be able to cover all of the land in a layer of gold up to your knees.',
        '2': 'The average person spends 6 months of their lifetime waiting on a red light to turn green.',
        '3': 'You burn more calories sleeping than you do watching television.',
        '4': 'There are more lifeforms living on your skin than there are people on the planet.',
        '5': 'In 1386 a pig in France was executed by public hanging for the murder of a child.',
        '6': 'A single cloud can weight more than 1 million pounds.',
        '7': 'The average person walks the equivalent of three times around the world in a lifetime.',
        '8': 'Coca-Cola would be green if coloring wasn’t added to it.',
        '9': 'Men are 6 times more likely to be struck by lightning than women.',
        '10': ' A sneeze travels about 100 miles per hour.',
    }
    speak(fact[x])
    return
