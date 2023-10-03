import tkinter as tk
import csv
import tkinter.messagebox
from tkinter import ttk, filedialog
from tkinter.simpledialog import askstring
import re
from jinja2 import Template
import barcode
from barcode.writer import ImageWriter
dictionary_data = None
blacklist_data = None
dicfilepath = None
def load_csv(filename):
    global dicfilepath
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")], title="Load "+filename)

    if file_path:
        try:
            # Open the CSV file and read its contents
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)


            # Display the imported data in a messagebox
            tk.messagebox.showinfo("CSV Import", f"CSV file imported successfully:\n\n{data[:5]}")

        except Exception as e:
            # Display an error message if the file cannot be imported
            tk.messagebox.showerror("Error", f"Failed to import CSV file:\n\n{str(e)}")
    if filename == 'dictionary.csv':
        dicfilepath = file_path
        print(dicfilepath)

    return data


def save_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def create_table(root, data):
    headings = data[0]
    data = data[1:]

    num_rows = len(data)
    num_cols = len(headings)

    table = tk.ttk.Treeview(root, show="headings")

    table["columns"] = tuple(str(i) for i in range(num_cols))

    for i, heading in enumerate(headings):
        table.column(str(i), width=150, anchor=tk.CENTER)
        table.heading(str(i), text=heading)

    for row in data:
        table.insert("", tk.END, values=tuple(row))
    treeScroll = tk.ttk.Scrollbar(root)
    treeScroll.configure(command=table.yview)
    table.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

    table.pack(pady=10, padx= 50)

    return table


def add_entry(table, entry, data):
    table.insert("", tk.END, values=tuple(entry))
    data.append(entry)


def delete_entry(table, data, filename):
    selected_item = table.selection()
    if selected_item:
        selected_row = table.index(selected_item)+1
        deleted_row = data.pop(selected_row)
        table.delete(selected_item)
        save_csv(filename, data)
        print(f"The entry '{deleted_row}' has been deleted from the CSV file.")


def clear_entries(entry_widgets):
    for entry in entry_widgets:
        entry.delete(0, tk.END)


def save_entries(filename, data, entry_widgets, table):
    new_entry = [entry.get() for entry in entry_widgets]
    add_entry(table, new_entry, data)
    save_csv(filename, data)
    clear_entries(entry_widgets)


def open_program():
    global dictionary_data
    filename = "dictionary.csv"

    # Check if the data is already imported
    if not dictionary_data:
        # Load the data from the file
        dictionary_data = load_csv(filename)

    root = tk.Tk()
    root.title("Dictionary")

    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    table = create_table(table_frame, dictionary_data)

    entry_widgets = []
    for _ in range(len(dictionary_data[0])):
        entry = tk.Entry(entry_frame, width=15)
        entry.pack(side=tk.LEFT, padx=5)
        entry_widgets.append(entry)

    add_button = tk.Button(button_frame, text="Add Entry",
                           command=lambda: save_entries(filename, dictionary_data, entry_widgets, table))
    add_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Entry", command=lambda: delete_entry(table, dictionary_data, filename))
    delete_button.pack(side=tk.LEFT, padx=5)


    root.mainloop()

def open_blacklist():
    global blacklist_data
    filename = "blacklist.csv"

    # Check if the data is already imported
    if not blacklist_data:
        # Load the data from the file
        blacklist_data = load_csv(filename)

    root = tk.Tk()
    root.title("Blacklist")

    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    table = create_table(table_frame, blacklist_data)

    entry_widgets = []
    for _ in range(len(blacklist_data[0])):
        entry = tk.Entry(entry_frame, width=15)
        entry.pack(side=tk.LEFT, padx=5)
        entry_widgets.append(entry)

    add_button = tk.Button(button_frame, text="Add Entry",
                           command=lambda: save_entries(filename, blacklist_data, entry_widgets, table))
    add_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Entry", command=lambda: delete_entry(table, blacklist_data, filename))
    delete_button.pack(side=tk.LEFT, padx=5)


    root.mainloop()

def png():


    root = tk.Tk()
    root.title("Create PNG")
    canvas1 = tk.Canvas(root, width=400, height=500)
    canvas1.pack()
    enname = tk.Entry(root)
    canvas1.create_window(300, 10, window=enname)
    namd = tk.Label(root, text="English Name")
    canvas1.create_window(100, 10, window=namd)
    cnname = tk.Entry(root)
    canvas1.create_window(300, 30, window=cnname)
    nam = tk.Label(root, text="Chinese Name")
    canvas1.create_window(100, 30, window=nam)
    productno = tk.Entry(root)
    canvas1.create_window(300, 50, window=productno)
    productnum = tk.Label(root, text="Product Code")
    canvas1.create_window(100, 50, window=productnum)
    energy = tk.Entry(root)
    canvas1.create_window(300, 70, window=energy)
    en = tk.Label(root, text="Energy (kcal)")
    canvas1.create_window(100, 70, window=en)
    fat = tk.Entry(root)
    canvas1.create_window(300, 90, window=fat)
    fats = tk.Label(root, text="Fat (g)")
    canvas1.create_window(100, 90, window=fats)
    saturates = tk.Entry(root)
    canvas1.create_window(300, 110, window=saturates)
    sat = tk.Label(root, text="of which saturates (g)")
    canvas1.create_window(100, 110, window=sat)
    carbohydrate = tk.Entry(root)
    canvas1.create_window(300, 130, window=carbohydrate)
    carbs = tk.Label(root, text="Carbohydrate (g)")
    canvas1.create_window(100, 130, window=carbs)
    sugars = tk.Entry(root)
    canvas1.create_window(300, 150, window=sugars)
    sug = tk.Label(root, text="of which sugars (g)")
    canvas1.create_window(100, 150, window=sug)
    fibre = tk.Entry(root)
    canvas1.create_window(300, 170, window=fibre)
    fib = tk.Label(root, text="Fibre (g)")
    canvas1.create_window(100, 170, window=fib)
    protein = tk.Entry(root)
    canvas1.create_window(300, 190, window=protein)
    prot = tk.Label(root, text="Protein (g)")
    canvas1.create_window(100, 190, window=prot)
    salt = tk.Entry(root)
    canvas1.create_window(300, 210, window=salt)
    salts = tk.Label(root, text="Salt (g)")
    canvas1.create_window(100, 210, window=salts)
    instruct = tk.Text(root, height=5, wrap=tk.WORD, width=50)
    instructions = tk.Label(root, text="Directions to use")
    canvas1.create_window(200, 390, window=instruct)
    canvas1.create_window(100, 330, window=instructions)
    country = tk.Entry(root)
    canvas1.create_window(300, 230, window=country)
    countryorigin = tk.Label(root, text="Country of Origin")
    canvas1.create_window(100, 230, window=countryorigin)
    initial_text = "China"
    country.insert(0, initial_text)
    barcod = tk.Entry(root)
    canvas1.create_window(300, 250, window=barcod)
    bar = tk.Label(root, text="Barcode")
    canvas1.create_window(100, 250, window=bar)
    weight = tk.Entry(root)
    canvas1.create_window(300, 270, window=weight)
    weig = tk.Label(root, text="Weight (g)")
    canvas1.create_window(100, 270, window=weig)
    bestbefore = tk.Entry(root)
    canvas1.create_window(300, 290, window=bestbefore)
    best = tk.Label(root, text="Best Before")
    canvas1.create_window(100, 290, window=best)
    combo = ttk.Combobox(root,
        state="readonly",
        values=["Once opened, keep in an airtight container.", "Once opened, keep refrigerated use within 4 weeks.","Once opened, use immediately."]
    )
    canvas1.create_window(300, 310, window=combo)
    storage = tk.Label(root, text="Storage")
    canvas1.create_window(100, 310, window=storage)


    def Generate():
        with open('label.html') as file:
            template_content = file.read()
        template = Template(template_content)
        items = [item.strip() for item in x.split(',')]

        # Create a list to hold the formatted ingredients
        formatted_ingredients = []

        # Process each ingredient and apply bold formatting if necessary
        for item in items:
            if '*' in item:
                parts = item.split('*')
                formatted_ingredients.append(parts[0] + '*<strong>' + parts[1] + '</strong>')
            else:
                formatted_ingredients.append(item)

        # Join the formatted ingredients with commas
        ingredients = ', '.join(formatted_ingredients)
        print(ingredients)

        def generate_barcode(barcode_number):
            # Generate the barcode object
            barcode_obj = barcode.get_barcode_class('ean13')
            barcode_image = barcode_obj(barcode_number, writer=ImageWriter())

            # Save the barcode image
            barcode_filename = f"{barcode_number}"
            barcode_image.save(barcode_filename)

            return barcode_filename

        # Example usage:
        barcode_number = barcod.get()
        barcode_filename = generate_barcode(barcode_number)
        print(barcode_filename)
        print(cnname.get())

        data = {
            'english': enname.get(),
            'chinese': cnname.get(),
            'energy': energy.get() + 'kcal' + '/' + str(round(int(energy.get())*4.184)) + 'kJ',
            'fat': fat.get() + 'g',
            'saturates': saturates.get() + 'g',
            'carbs': carbohydrate.get() + 'g',
            'sugars': sugars.get() + 'g',
            'proteins': protein.get() + 'g',
            'salt': salt.get() + 'g',
            'barcode_image_path': barcode_filename+'.png',
            'country': country.get(),
            'ingredients': ingredients,
            'net_weight': weight.get() + 'g',
            'product_number': productno.get(),
            'storage_instructions': 'Store in a cold and dry place. '+combo.get(),
            'instructions': instruct.get(1.0, tkinter.END),
            'best_before_date': bestbefore.get()
        }

        rendered_html = template.render(**data)

        string = (productno.get()+'.html')
        with open(string, 'x', encoding="utf-8") as file:
            file.write(rendered_html)
        print(string,"file created")

    process = tk.Button(root, text="Process", command=Generate)
    process.pack()





def main():
    root = tk.Tk()
    root.title("CSV Program")

    menu = tk.Menu(root)
    root.config(menu=menu)

    def translate_text():
        global dictionary_data, blacklist_data  # Add global variables to store the imported data

        filename = "dictionary.csv"
        blacklist = "blacklist.csv"

        # Check if the data is already imported
        if dictionary_data is None:
            dictionary_data = load_csv(filename)

        if blacklist_data is None:
            blacklist_data = load_csv(blacklist)
        listed = False
        count = 0
        user_input = text_box.get("1.0", tk.END).strip()
        words = user_input.split('/')
        global none

        none = []
        translated_words = []
        for word in words:
            found = False
            listed = True

            for row in dictionary_data:
                if "%" in word.lower():
                    print("Yes")
                    print(str(word.lower()).split('%')[0].rstrip().split()[0])
                    if row[0].lower() == str(word.lower()).split('%')[0].rstrip().split()[0]:
                        translated_words.append(row[1]+" ("+re.findall(r'\d+%', word.lower())[0]+")")
                        found = True
                        break

                else:
                    if row[0].lower() == word.lower():
                        translated_words.append(row[1])
                        print(translated_words)
                        print(words)
                        found = True
                        break
            for row in blacklist_data:
                count = 0
                alternate = False
                if row[0].lower() == word.lower():
                    tkinter.messagebox.showinfo(message="PROHIBITED SUBSTANCE:"+word)
                    numeric_value = ''.join(filter(str.isdigit, row[1]))
                    if numeric_value:
                        results = int(numeric_value)
                    while alternate is False:
                        count+=1
                        ans = "e"+(str(results+count))
                        print(ans)
                        for row in dictionary_data:
                            if ans in row[1].lower():
                                print("match found", row[1].lower())
                                string = ("Use",row[1].lower(),"instead?")
                                res = tk.messagebox.askquestion('Replace', string)
                                if res == "yes":
                                    translated_words.append(row[1].lower())
                                    alternate = True
                                else:
                                    pass
                        found = True

            if not found:
                translated_words.append(f"[{word}]")
                none.append(word)
                print(none)


        translated_text = ", ".join(translated_words)

        result.delete("1.0", tk.END)
        result.insert(tk.END, translated_text)
        result.tag_remove("bold", "1.0", tk.END)

        # List of allergy-related words
        allergy_words = [
            "Milk",
            "Eggs",
            "Egg",
            "Fish",
            "Crustacean Shellfish",
            "Tree Nuts",
            "Peanuts",
            "Wheat",
            "Soybeans",
            "Sesame",
            "Mustard",
            "Celery",
            "Lupin",
            "Sulphites",
            "Molluscs",
            "Celery",
            "Rye",
            "Flour",
            "Oats",
            "Barley",
            "Noodles",
            "Crabs",
            "Lobster",
            "Prawn",
            "Scampi",
            "Shrimp",
            "Fish",
            "Lupin",
            "Cream",
            "Cheese",
            "Butter",
            "Yogurt",
            "Mussels",
            "Squid",
            "Whelks",
            "Oyster",
            "Snails",
            "Mustard",
            "Nuts",
            "Cashew",
            "Almond",
            "Hazelnuts",
            "Peanuts",
            "Sesame",
            "Soy",
            "Raisins"
        ]
        # Apply bold formatting to allergy-related words
        for word in allergy_words:
            start_index = "1.0"
            while True:
                start_index = result.search(word, start_index, tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(word)}c"
                result.tag_add("bold", start_index, end_index)
                first_occurrence_index = result.search(word, start_index, end_index)
                result.insert(first_occurrence_index, "*")
                start_index = end_index
        global x
        x = result.get("1.0", tk.END)
        print(x)



    def rectify():
        global dicfilepath, dictionary_data
        filename = 'dictionary.csv'
        print(none)
        if len(none) == 0:
            tkinter.messagebox.showinfo(message = "Nothing to rectify!")
        else:
            for i in range(len(none)):
                data = askstring("Translation for",none[i])
                with open(str(dicfilepath), 'a', newline='', encoding='utf-8') as file:
                    print("hello")
                    writer = csv.writer(file)
                    writer.writerow([none[i], data])


    global dictionary_data, blacklist_data
    def reimport():
        global dictionary_data, blacklist_data  # Add global variables to store the imported data

        filename = "dictionary.csv"
        blacklist = "blacklist.csv"
        dictionary_data = None
        blacklist_data = None

        # Check if the data is already imported
        if dictionary_data is None:
            dictionary_data = load_csv(filename)

        if blacklist_data is None:
            blacklist_data = load_csv(blacklist)


    program_menu = tk.Menu(menu)
    menu.add_cascade(label="Program", menu=program_menu)
    program_menu.add_command(label="Open Translations", command=open_program)
    program_menu.add_separator()
    program_menu.add_command(label="Open Blacklist", command=open_blacklist)
    program_menu.add_separator()
    program_menu.add_command(label="Re-Import", command=reimport)
    program_menu.add_separator()
    program_menu.add_command(label="Exit", command=root.quit)
    text_box = tk.Text(root, height=10, width=50)
    text_box.pack(pady=10)

    translate_button = tk.Button(root, text="Translate", command = translate_text)
    translate_button.pack()
    rectify_button = tk.Button(root, text="Rectify Errors", command = rectify)
    rectify_button.pack()
    result = tk.Text(root, height=10, width=50)
    result.pack(pady=10)
    result.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))


    create_png = tk.Button(root, text="Create HTML Label", command=png)
    create_png.pack()
    filename = "dictionary.csv"
    blacklist = "blacklist.csv"

    # Check if the data is already imported
    if dictionary_data is None:
        dictionary_data = load_csv(filename)

    if blacklist_data is None:
        blacklist_data = load_csv(blacklist)

    root.mainloop()


if __name__ == "__main__":
    main()