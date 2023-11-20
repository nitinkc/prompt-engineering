# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import OpenApiConnect as bp

import panel as pn  # GUI

pn.extension()

panels = []  # collect display

context = [{'role': 'system',
            'content': """
            Coffee Ordering System. A customer can order coffee with multiple \
            choices. Customer can have multiple additions of items \
            into the coffee
            
            Coffee choices:\
            Plain beverage : $5.0\
            Dark Roast : $5.5\
            Espresso : $6.0\
            Decaf : $4.5\
            
            Additions/With Choices
            Milk : $1.50\
            Soy Milk : $2.50\
            Sugar : $0.50\
            """
            }]  # accumulate messages

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(bp.collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dashboard
    # prompt = f"""
    # Translate the following English text into all Indian Languages: \
    # ```Hi, The train had left before I arrive at the station```
    # """
    # response = bp.get_completion(prompt)
    # print(response)
