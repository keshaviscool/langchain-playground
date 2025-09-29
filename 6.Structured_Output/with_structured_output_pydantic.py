from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(BaseModel):

    key_themes: list[str] = Field(description="write down all the key themes discussed in review in the list")
    summary: str = Field(description="a brief summary of review")
    sentiment: Literal["pos", "neg"] = Field(description="sentiment of the review: Negative, Positive or Neutral")
    pros: Optional[list[str]] = Field(default=None, description="write down all the pros")
    cons: Optional[list[str]] = Field(default=None, description="write down all the cons")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
This is, hands down, the worst excuse for a guitar I’ve ever seen in my life. The quality is beyond pathetic ,whoever manufactured this clearly has zero knowledge about how a guitar is actually made. The fretboard and string distance are completely messed up, making it unplayable. It’s like they just randomly slapped some wood and strings together and called it a “guitar.”

To make things worse, the bridge literally broke within 15-20 days. Imagine spending your hard-earned money just to watch your instrument self-destruct like a cheap toy. 🤦‍♂️ This isn’t just bad , it’s a straight-up scam.

DO NOT BUY THIS TRASH. Seriously, even if you are a beginner, stay far away. You’ll just waste your money and end up hating the guitar because of this garbage. Instead, go to a local music shop, where you can get a decent beginner guitar starting at around ₹3000.

To the so-called “manufacturers”:
If you don’t know the basic science of fret spacing or how to make a stable bridge,maybe stick to making chopping boards instead of ruining music.

Avoid this disaster at all costs.save yourself from headache and buy a proper instrument locally.this isn't just
A guitar,it's firewood with strings.
""")

print(result)
