# import img_to_text
# import pdf_to_text
# import audio_to_text
# import video_to_text
# import url_to_text
# import ppt_to_txt
# import preprocessing
# import get_media
# from langchain_cohere import ChatCohere
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# class CustomFlashcardGenerator:
#     def __init__(self):
#         self.text = ''
#         self.keywords = []

#     def process_img(self, file):
#         self.text = img_to_text.image_to_text(file)

#     def process_pdf(self, file):
#         self.text = pdf_to_text.pdf_to_text(file)

#     def process_audio(self, file):
#         self.text = audio_to_text.audio_to_text(file)

#     def process_video(self, file):
#         self.text = video_to_text.video_to_text(file)

#     def process_url(self, file):
#         self.text = url_to_text.url_to_text(file)
    
#     def process_ppt(self, file):
#         self.text=ppt_to_txt.ppt_to_text(file)

#     def get_text(self, file, filetype):
#         if filetype == 'img':
#             self.process_img(file)
#         elif filetype == 'pdf':
#             self.process_pdf(file)
#         elif filetype == 'audio':
#             self.process_audio(file)
#         elif filetype == 'video':
#             self.process_video(file)
#         elif filetype == 'url':
#             self.process_url(file)
#         elif filetype == 'text':
#             self.text = file
#         elif filetype == 'ppt':
#             self.process_ppt(file)
#         else:
#             raise ValueError(f"Unsupported file type: {filetype}")
    
#     def generate_questions_and_answers(self, qa_chain, grade, keywords):
#         # Join keywords into a comma-separated string
#         keywords_str = ", ".join(keywords)
        
#         # Generate questions and answers using the LangChain agent
#         response = qa_chain.invoke({"grade": grade, "keywords": keywords_str})  # Pass parameters as a dictionary

#         return response['text']

#     def structure_qa_output(self, raw_output):
#         """Convert raw output string into a list of dictionaries with questions and answers."""
#         qa_pairs = []
#         # Split the response into questions and answers based on double newlines
#         qa_blocks = raw_output.strip().split('\n\n')  # Split into blocks of Q&A
#         for block in qa_blocks:
#             lines = block.split('\n')  # Split each block into lines
#             if len(lines) >= 2:  # Ensure there are at least a question and an answer
#                 question = lines[0].split(": ", 1)[1]  # Extract question
#                 answer = lines[1].split(": ", 1)[1]  # Extract answer
#                 qa_pairs.append({"question": question, "answer": answer})  # Append to list as a dictionary
        
#         return qa_pairs
    
#     def get_keywords(self):
#         self.keywords = preprocessing.extract_keywords(self.text)
    
#     def get_images_video(self,structured_output):
#         for item in structured_output:
#             query=item['question']
#             image=get_media.get_image(query)
#             video=get_media.get_video_link(query)
#             item.update({'image':image})
#             # item.update({'video':video})
            
        
#         return structured_output

#     def give_custom_flashcard(self, api_key, grade):
#         # Initialize the language model with the Cohere API
#         llm = ChatCohere(cohere_api_key=api_key)

#         # Define a prompt template for generating questions and answers
#         prompt_template = PromptTemplate(
#             input_variables=["grade", "keywords"],
#             template="""
#             You are an educational assistant. Based on the following keywords and the student's grade level, generate a few questions with their corresponding answers.
#             If there are a lot of keywords, generate more questions and answers.

#             Grade Level: {grade}
#             Keywords: {keywords}

#             Please format your response as follows:
#             Question 1: [Question]
#             Answer 1: [Answer]
            
#             Question 2: [Question]
#             Answer 2: [Answer]
            
#             Question 3: [Question]
#             Answer 3: [Answer]
            
#             ...
            
#             """
#         )
        
#         # Create a chain that utilizes both the LLM and the prompt template
#         qa_chain = LLMChain(llm=llm, prompt=prompt_template)
        
#         # Ensure keywords are extracted before generating questions and answers
#         self.get_keywords()
        
#         qa_output = self.generate_questions_and_answers(qa_chain, grade, self.keywords)
#         # print(qa_output)
        
#         structured_output = self.structure_qa_output(qa_output)
        
#         output_with_images=self.get_images(structured_output)
        
#         return output_with_images


#     def give_flashcards(self,file_path, file_type, grade):
#         # Process the text input based on the provided file type
#         self.get_text(file_path, file_type)

#         # Replace with your actual Cohere API key here
#         api_key = "RxSPixDw28aNcvuOvUJivFUiepCOiByY4eBmrY2p"
        
#         # Generate flashcards based on extracted keywords from given text content
#         flashcard_output = self.give_custom_flashcard(api_key=api_key, grade=grade)

#         return flashcard_output




# # Example usage
# generator = CustomFlashcardGenerator()

# # file_path = "example.pdf"  # Replace with your file path
# # file_type = "pdf"  # Replace with your file type
# file='''Alcohols are an important class of organic compounds that contain a hydroxyl group (-OH) bonded to a carbon atom. They are derived from hydrocarbons by replacing one or more hydrogen atoms with hydroxyl groups. Alcohols are widely used in everyday life, from hand sanitizers to fuels.

# The general formula for alcohols is R-OH, where R represents an alkyl group (such as methyl, ethyl, or propyl). The simplest alcohol is methanol (CH3OH), followed by ethanol (C2H5OH), which is commonly known as drinking alcohol.

# Alcohols are classified into three types based on the number of carbon atoms attached to the carbon bearing the hydroxyl group:

# Primary alcohols: The carbon atom with the -OH group is attached to only one other carbon atom.
# Secondary alcohols: The carbon atom with the -OH group is attached to two other carbon atoms.
# Tertiary alcohols: The carbon atom with the -OH group is attached to three other carbon atoms.
# Alcohols have higher boiling points compared to hydrocarbons of similar molecular mass due to hydrogen bonding between alcohol molecules. They are generally soluble in water, with solubility decreasing as the length of the carbon chain increases.

# Common reactions of alcohols include:

# Oxidation: Alcohols can be oxidized to form aldehydes, ketones, or carboxylic acids.
# Dehydration: Alcohols can undergo dehydration to form alkenes.
# Esterification: Alcohols react with carboxylic acids to form esters.
# Alcohols have numerous applications in industry and everyday life. Ethanol is used as a solvent, fuel additive, and in alcoholic beverages. Methanol is used in antifreeze and as a fuel. Isopropyl alcohol is commonly used as a disinfectant and cleaning agent.

# Understanding the properties and reactions of alcohols is crucial for further studies in organic chemistry and biochemistry.'''

# file_type='text'

# # file='/home/yuvraj/Coding/OverloadOblivion_Datahack/data/image.png'
# # file='/home/yuvraj/Coding/OverloadOblivion_Datahack/data/Saurav_Resume (7).pdf'
# # file="/home/yuvraj/Coding/OverloadOblivion_Datahack/data/ch 1.pptx"

# flashcard_text = generator.give_flashcards(file, 'text','11')

# # # # Print out structured flashcard output
# print("Generated Flashcards:")
# for flashcard in flashcard_text:
#     # print(f"Q: {flashcard['question']}\nA: {flashcard['answer']}\n")
#     print(flashcard)

import asyncio
from . import img_to_text
from . import pdf_to_text
from . import audio_to_text
from . import video_to_text
from . import url_to_text
from . import ppt_to_txt
from . import preprocessing
from . import get_media
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class CustomFlashcardGenerator:
    def __init__(self,youtube_api_key,cohere_api_key):
        self.text = ''
        self.keywords = []
        self.youtube_api_key=youtube_api_key
        self.cohere_api_key=cohere_api_key

    async def process_img(self, file):
        self.text = await asyncio.to_thread(img_to_text.image_to_text, file)

    async def process_pdf(self, file):
        self.text = await asyncio.to_thread(pdf_to_text.pdf_to_text, file)

    async def process_audio(self, file):
        self.text = await asyncio.to_thread(audio_to_text.audio_to_text, file)

    async def process_video(self, file):
        self.text = await asyncio.to_thread(video_to_text.video_to_text, file)

    async def process_url(self, file):
        self.text = await asyncio.to_thread(url_to_text.url_to_text, file)
    
    async def process_ppt(self, file):
        self.text = await asyncio.to_thread(ppt_to_txt.ppt_to_text, file)

    async def get_text(self, file, filetype):
        if filetype == 'img':
            await self.process_img(file)
        elif filetype == 'pdf':
            await self.process_pdf(file)
        elif filetype == 'audio':
            await self.process_audio(file)
        elif filetype == 'video':
            await self.process_video(file)
        elif filetype == 'url':
            await self.process_url(file)
        elif filetype == 'text':
            self.text = file
        elif filetype == 'ppt':
            await self.process_ppt(file)
        else:
            raise ValueError(f"Unsupported file type: {filetype}")

    async def generate_questions_and_answers(self, qa_chain, grade, keywords):
        keywords_str = ", ".join(keywords)
        response = await asyncio.to_thread(qa_chain.invoke, {"grade": grade, "keywords": keywords_str})
        return response['text']

    async def structure_qa_output(self, raw_output):
        qa_pairs = []
        qa_blocks = raw_output.strip().split('\n\n')
        for block in qa_blocks:
            lines = block.split('\n')
            if len(lines) >= 2:
                question = lines[0].split(": ", 1)[1]
                answer = lines[1].split(": ", 1)[1]
                qa_pairs.append({"question": question, "answer": answer})
        return qa_pairs

    async def get_keywords(self):
        self.keywords = await asyncio.to_thread(preprocessing.extract_keywords, self.text)

    async def get_images_video(self, structured_output):
        for item in structured_output:
            query = item['question']
            image = await asyncio.to_thread(get_media.get_image, query)
            video = await asyncio.to_thread(get_media.get_video_link, query,self.youtube_api_key)
            item.update({'image': image})
            item.update({'video': video})
        return structured_output

    async def give_custom_flashcard(self, grade):
        llm = ChatCohere(cohere_api_key=self.cohere_api_key)
        prompt_template = PromptTemplate(
            input_variables=["grade", "keywords"],
            template="""
            You are an educational assistant. Based on the following keywords and the student's grade level, generate a few questions with their corresponding answers.
            If there are a lot of keywords, generate more questions and answers.
cohere_api_key,
            Grade Level: {grade}
            Keywords: {keywords}

            Please format your response as follows:
            Question 1: [Question]
            Answer 1: [Answer]
            
            Question 2: [Question]
            Answer 2: [Answer]
            
            Question 3: [Question]
            Answer 3: [Answer]
            
            ...
            """
        )
        
        qa_chain = LLMChain(llm=llm, prompt=prompt_template)
        await self.get_keywords()
        qa_output = await self.generate_questions_and_answers(qa_chain, grade, self.keywords)
        structured_output = await self.structure_qa_output(qa_output)
        output_with_images = await self.get_images_video(structured_output)
        return output_with_images

    async def give_flashcards(self, file_path, file_type, grade):
        await self.get_text(file_path, file_type)
        # api_key = "RxSPixDw28aNcvuOvUJivFUiepCOiByY4eBmrY2p"
        flashcard_output = await self.give_custom_flashcard(grade)
        return flashcard_output

# # Example usage
# generator = CustomFlashcardGenerator()

# file = '''Alcohols are an important class of organic compounds that contain a hydroxyl group (-OH) bonded to a carbon atom. They are derived from hydrocarbons by replacing one or more hydrogen atoms with hydroxyl groups. Alcohols are widely used in everyday life, from hand sanitizers to fuels.

# The general formula for alcohols is R-OH, where R represents an alkyl group (such as methyl, ethyl, or propyl). The simplest alcohol is methanol (CH3OH), followed by ethanol (C2H5OH), which is commonly known as drinking alcohol.

# Alcohols are classified into three types based on the number of carbon atoms attached to the carbon bearing the hydroxyl group:

# Primary alcohols: The carbon atom with the -OH group is attached to only one other carbon atom.
# Secondary alcohols: The carbon atom with the -OH group is attached to two other carbon atoms.
# Tertiary alcohols: The carbon atom with the -OH group is attached to three other carbon atoms.
# Alcohols have higher boiling points compared to hydrocarbons of similar molecular mass due to hydrogen bonding between alcohol molecules. They are generally soluble in water, with solubility decreasing as the length of the carbon chain increases.

# Common reactions of alcohols include:

# Oxidation: Alcohols can be oxidized to form aldehydes, ketones, or carboxylic acids.
# Dehydration: Alcohols can undergo dehydration to form alkenes.
# Esterification: Alcohols react with carboxylic acids to form esters.
# Alcohols have numerous applications in industry and everyday life. Ethanol is used as a solvent, fuel additive, and in alcoholic beverages. Methanol is used in antifreeze and as a fuel. Isopropyl alcohol is commonly used as a disinfectant and cleaning agent.

# Understanding the properties and reactions of alcohols is crucial for further studies in organic chemistry and biochemistry.'''

# file_type = 'text'

# flashcard_text = asyncio.run(generator.give_flashcards(file, file_type, '11'))

# # Print out structured flashcard output
# print("Generated Flashcards:")
# for flashcard in flashcard_text:
#     print(flashcard)