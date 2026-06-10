from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()


def main():
    
    information = """
    Elon Musk is a businessman and entrepreneur, known predominantly for his leading roles in the automotive company Tesla, Inc. and the space company SpaceX. Musk is also known for his ownership of technology company X Corp. and his role in the founding of The Boring Company, xAI, Neuralink, and OpenAI.

In 1995, Musk, co-founded what would later be known as Zip2, later selling the company to Compaq for $307 million in 1999. Receiving $22 million in the process, Musk used $12 million of the proceedings to co-found the e-payment company X.com that same year. In 2000, X.com merged with the online bank Confinity and was rebranded as PayPal. In 2002, Musk received $176 million after PayPal acquired eBay as the company's largest shareholder, and would much later purchase the X.com domain from PayPal, with the intention of creating an "everything app". In 2004, with an investment of $6.3 million, Musk then became the chairman and majority shareholder of Tesla. In 2016, Musk co-founded the neurotechnology startup company Neuralink, with an investment of $100 million, followed by founding the Boring Company to construct tunnels. In 2022, Musk completed his acquisition of Twitter, becoming the CEO of Twitter, prior to its rebranding to X.

Beginning with his involvement with space exploration companies in early 2001, he founded SpaceX in 2002, with the company attempting the first rocket launch in 2006. Since 2019, SpaceX been developing Starship, a reusable, super heavy-lift launch vehicle, and in 2015, they began development of the Starlink for satellite Internet access. Having sent Starlink terminals to Ukraine in 2022, Musk refused to block Russian state media on Starlink and later faced criticism over denying access over Crimea.

With Tesla, he assumed leadership as CEO and product architect in 2008. In 2018, Musk was sued by the SEC for a tweet stating that funding had been secured for potentially taking Tesla private, later settling with the SEC, with Musk stepping down as Tesla chairman while remaining its CEO. In 2023, shareholders filed a lawsuit, and a jury subsequently found Musk and Tesla not liable. As of 2019, Musk was the longest-tenured CEO of any automotive manufacturer globally, and under the CEO, Tesla has also constructed multiple lithium-ion battery and electric vehicle factories, named Gigafactories.[1]
    """

    summary_template = """
    given the information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model='gpt-4.1-mini')
    chain = summary_prompt_template | llm
    response = chain.invoke(input={'information': information})
    print(response.content)


    



if __name__ == "__main__":
    main()
