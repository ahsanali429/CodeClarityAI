import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# LLM
llm = CTransformers(model='/Users/ahsanali/development/project/llm/models/mistral-7b-instruct-v0.2.Q8_0.gguf',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})


def getLLMResponse(prompt_text, input_code):

    ## Prompt Template
    template="""
        You are a helpful assistant for a developer, please {prompt_text} {input_code}
        within 200 words.
            """
    
    prompt=PromptTemplate(input_variables=["prompt_text", "input_code"],
                          template=template)
    
    ## Generate the response from the LLM
    response=llm(prompt.format(prompt_text=prompt_text,input_code=input_code))
    print(response)
    return response



st.set_page_config(page_title="CodeClarityAI: AI Assistant for Code Analysis",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("CodeClarityAI: AI Assistant for Code Analysis 🤖")

input_text=st.text_area("Enter Your code", placeholder="Insert your code here...")

col1, col2 , col3, col4 = st.columns([1,1,1,1])

with col1:
    summary=st.button("Summary")
with col2:
    explaination=st.button("Explaination")
with col3:
    optimize=st.button("Optimise")
with col4:
    lang_detect=st.button("Language Detection")

st.markdown("---")

# Button Actions
if lang_detect:
    st.write(getLLMResponse(f"Don't give any explanation, Only Identify the programming language and name it: ", {input_text}) or "No Response!!!")
if summary:
    st.write(getLLMResponse(f"Provide a single-sentence summary of the following code within 20 words: ", {input_text}) or "No Response!!!")
if explaination:
    st.write(getLLMResponse(f"Explain the following code: ", {input_text}) or "No Response!!!")
if optimize:
    st.write(getLLMResponse(f"Provide me the optimized code for this code: ", {input_text}) or "No Response!!!")


# Footer
st.markdown("---")
st.write("© 2024 CodeClarityAI: AI Assistant For Code Analysis")