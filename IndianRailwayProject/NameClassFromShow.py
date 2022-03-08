import pandas as pd

def generate(filename):
    df = pd.read_excel(filename)
    print(df)
    print("***************************************")
    for index,item in df.iterrows():
            print(index)
            file=open(f"{index}_{item['name']}.txt",'w')
            file.write(f"My Name is {item['name']}\ni am From {item['from']}\ni am in {item['class']}th Class\n")

if __name__ == '__main__':
    generate("Name_Finder.xlsx")
