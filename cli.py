"""
Module that contains the command line app.
"""
import argparse
from art import text2art
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

#############################################################################
#                            Initialize the model                           #
model = GenerativeModel(model_name="gemini-1.5-flash-001",)
generation_config = GenerationConfig(
    temperature=0.01
)
#############################################################################


# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")

def main(args=None):

    try:
        print("\n")
        art = text2art("AC215")
        print(art)
        print("\n")
        print("Arguments:", args)
        text = args.text
        text = text.replace("+"," ")

        print("\n\n")
        print("Input:", text)

        #results = translator.translate(text, src=args.src, dest=args.dest)
        #print("Output:", results.text)

        # Generate output
        input_prompt = f"""
            Translate the following text from source language code {args.src} to destination language code {args.dest}
            {text}
        """
        print(input_prompt,"\n\n\n")
        response = model.generate_content(input_prompt,generation_config=generation_config)
        paragraph = response.text


        print("Generated text:")
        print(paragraph)

    except Exception as e:
        print(f"Error occurred while generating content: {e}")


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="A simple translation app")

    parser.add_argument(
        "-t", "--text", type=str, default="I love cheese", help="Text to translate"
    )
    parser.add_argument("-s", "--src", default="en", help="Source Language")
    parser.add_argument("-d", "--dest", default="it", help="Destination Language")

    args = parser.parse_args()

    main(args)
