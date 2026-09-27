from hf import generate_response
def run_activity():
    print("ZERO-SHOT,ONE-SHOT &FEW-SHOT LEARNING ACTIVITY")
    category=input('Enter a category(e.g animal,food,city): ').strip()
    item=input(f"Enter a specific {category} to classify : ").strip()
    if not category or not item:
        print("Please fill both thr fileds to run the activity ")
        return
    zero_shot=f"Is {item} a {category}?Answer Yes or no."
    print("\n_____Zero shot learning______")
    print(f"Response:{generate_response(zero_shot,temperature=0.3,max_tokens=1024)}")
    one_shot=f"Examples:Category:fruit Item:apple answer:yes apple is a fruit\n now you try: category:{category} Item:{item} Answer:""" 
    print("\n One shot Learning")
    print(f"Response:{generate_response(one_shot,temperature=0.3,max_tokens=1024)}""")
    
    few_shot=f"Example1:Category:fruit Item:apple answer:yes apple is a fruit\n Now you try:Category:{category},Item:{item}Answer: """ 
    print("\nFew shot learning")
    print(f"Response:{generate_response(few_shot,temperature=0.3,max_tokens=1024)}")
    creative_prompt=f"""write a one sentence story about the given word. 
    Example1:Wood:moon
    Story:The moon winked at the lovers as they shared their first kiss.
    word:{item}
    Story:"""
    print("\n  Creative few shot")
    print(f"Respponse:{generate_response(creative_prompt,temperature=0.7,max_tokens=1024)}")
    print("\n REFLECTION QUESTIONS")
    print("1.Howd did the response differ between zero-shot,one-shot and few shot? ")
    print("2.Which approach gave the most useful response?")
    print("3.How did the examples influence the models output?")
if __name__=="__main__":
    run_activity()