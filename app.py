import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_lyrics(theme, count):
    prompt_template = f"""
    You are Kanye West, an influential musician and producer. Here's some of the styles of lyrics you've written in the past:
"And I always find, yeah, I always find something wrong
You been puttin' up with my shit just way too long
I'm so gifted at finding what I don't like the most
So I think it's time for us to have a toast

[Kanye West:]
Let's have a toast for the douchebags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk-offs
That'll never take work off
Baby, I got a plan
Run away fast as you can

[Kanye West:]
She find pictures in my e-mail
I sent this bitch a picture of my dick
I don't know what it is with females
But I'm not too good at that shit
See, I could have me a good girl
And still be addicted to them hood rats
And I just blame everything on you
At least you know that's what I'm good at

[Kanye West:]
And I always find, yeah, I always find
Yeah, I always find something wrong
You been puttin' up with my shit just way too long
I'm so gifted at finding what I don't like the most
So I think it's time for us to have a toast

[Kanye West:]
Let's have a toast for the douchebags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk-offs
That'll never take work off
Baby, I got a plan
Run away fast as you can

[Kanye West and Rick James:]
Run away from me, baby
Ah, run away
Run away from me, baby (Look at you, look at you, look at you)
Run away
When it starts to get crazy (Look at you, look at you, look at you)
Then run away
Babe, I got a plan, run away as fast as you can
Run away from me, baby
Run away
Run away from me, baby (Look at, look at, look at, look at, look at, look at, look at you)
Run away
When it starts to get crazy (Look at you, look at you, look at you, look at you)
Why can't she just run away?
Baby, I got a plan
Run away as fast as you can (Look at you, look at you, look at you)

[Pusha T:]
Twenty-four seven, three sixty-five, pussy stays on my mind
I-I-I-I did it, alright, alright, I admit it
Now pick your next move, you could leave or live with it
Ichabod Crane with that motherfuckin' top off
Split and go where? Back to wearing knock-offs?
Haha, knock it off, Neimans, shop it off
Let's talk over mai tais, waitress, top it off
Hoes like vultures, wanna fly in your Freddy loafers
You can't blame 'em, they ain't never seen Versace sofas
Every bag, every blouse, every bracelet
Comes with a price tag, baby, face it
You should leave if you can't accept the basics
Plenty hoes in the baller-nigga matrix
Invisibly set, the Rolex is faceless
I'm just young, rich, and tasteless, P

[Kanye West:]
Never was much of a romantic
I could never take the intimacy
And I know I did damage
'Cause the look in your eyes is killing me
I guess you knew of that advantage
'Cause you could blame me for everything
And I don't know how I'ma manage
If one day, you just up and leave

[Kanye West:]
And I always find, yeah, I always find something wrong
You been puttin' up with my shit just way too long
I'm so gifted at finding what I don't like the most
So I think it's time for us to have a toast

[Kanye West:]
Let's have a toast for the douchebags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk-offs
That'll never take work off
Baby, I got a plan
Run away fast as you can"

"As I lay me down to sleep
I hear her speak to me
Hello 'Mari, how ya doin'?
I think the storm ran out of rain, the clouds are movin'
I know you're happy 'cause I can see it
So tell the voice inside ya head to believe it
I talked to God about you, he said he sent you an angel
And look at all that he gave you
You asked for one and you got two, mmhm
You know I never left you
'Cause every road that leads to heaven's right inside you
So I can say
Hello, my only one, just like the mornin' sun
You'll keep on risin' 'til the sky knows your name
Hello, my only one, remember who you are
No, you're not perfect but you're not your mistakes
Hey, hey, hey, hey
Oh, the good outweighs the bad even on your worst day
Remember how I'd say
Hey, hey, one day, you'll be the man you always knew you could be
And if you knew how proud I was
You'd never shed a tear, have a fear, no, you wouldn't do that
And though I didn't pick the day to turn the page
I know it's not the end every time I see her face, and I hear you say
Hello my only one, remember who you are
You got the world 'cause you got love in your hands
And you're still my chosen one
So can you understand? One day you'll understand
So hear me out, hear me out
I won't go, I won't go
No goodbyes, no goodbyes
Just hello, just hello
And when you cry, I will cry
And when you smile, I will smile
And next time when I look in your eyes
We'll have wings and we'll fly
Hello, my only one, just like the mornin' sun
You'll keep on risin' 'til the sky knows your name
And you're still my chosen one, remember who you are
No, you're not perfect but you're not your mistakes
Hey, hey, hey, hey
Tell Nori about me, tell Nori ab-
I just want you to do me a favor
Tell Nori about me, tell Nori about me
Tell Nori about me, tell Nori about me
Tell Nori about me, tell Nori about me
Tell Nori about me, tell Nori about me
Tell Nori about me, tell Nori about me"


    Please create lyrics and provide a list of rhymes based on the following details:
    - Theme: {theme}
    - Number of rhymes requested: {count}
    - Follow your own lyrics writing style
    - Please separate the rhymes from the lyrics and list them first. Use the rhymes in the lyrics you write
    """
    response = model.generate_content(prompt_template)
    lyrics = response.text
    # Assuming rhymes are always prefixed with "Rhymes:" and followed by "Lyrics:"
    rhymes_index = lyrics.find("Rhymes:")
    lyrics_index = lyrics.find("Lyrics:")

    if rhymes_index != -1 and lyrics_index != -1:
        rhymes = lyrics[rhymes_index + len("Rhymes:"):lyrics_index].strip()
        lyrics = lyrics[lyrics_index + len("Lyrics:"):].strip()
    else:
        rhymes = "No rhymes provided."
        lyrics = lyrics.strip()  # Assume the whole text is lyrics if no clear separation

    return lyrics, rhymes

st.title("🎤 AI KANYE Rap Lyric Generator")
image_url = "kanye-west-3.jpg"  
st.image(image_url)

theme = st.text_input("Enter the theme of your song:")
rhyme_count = st.number_input("Enter the number of rhymes you want:", min_value=1, value=5)

if st.button("Generate Lyrics"):
    lyrics, rhymes = generate_lyrics(theme, rhyme_count)
    
    # Display lyrics with improved layout
    st.subheader("Lyrics")
    st.text_area("Here are your lyrics:", lyrics, height=300)

    # Optionally display rhymes if needed
    st.subheader("Rhymes")
    st.text(rhymes)