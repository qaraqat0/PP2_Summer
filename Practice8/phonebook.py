import re
from connect import get_connection


class PhoneBook:
    def __init__(self):
        pass

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("CALL upsert_contact(%s::text, %s::text)", (name, phone))

        conn.commit()
        cur.close()
        conn.close()

    print("Contact added or updated.")

    def add_many_contacts(self):
        names = []
        phones = []
        bad = []

        count = int(input("How many contacts do you want to add? "))

        for i in range(count):
            print(f"\nContact {i + 1}")
            nm = input("Name: ")
            ph = input("Phone: ")

            if re.match(r'^\+?[0-9]{10,15}$', ph):
                names.append(nm)
                phones.append(ph)
            else:
                bad.append((nm, ph))

        if bad:
            print("\nIncorrect data (not added):")
        for nm, ph in bad:
            print(nm, ph)

        if names:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "CALL insert_many_contacts(%s::text[], %s::text[])",
                (names, phones)
            )
            conn.commit()
            cur.close()
            conn.close()

        print("Contacts import finished.")
       
    def show_all(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM contacts ORDER BY id")
        rows = cur.fetchall()

        if len(rows) == 0:
            print("No contacts.")
        else:
            for row in rows:
                print(row)

        cur.close()
        conn.close()

    def find_by_pattern(self):
        patt = input("Enter pattern: ")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM search_contacts(%s::text)", (patt,))
        rows = cur.fetchall()

        if len(rows) == 0:
            print("Nothing found.")
        else:
            for row in rows:
                print(row)

        cur.close()
        conn.close()

    def show_paginated(self):
        lim = int(input("Enter limit: "))
        offs = int(input("Enter offset: "))

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s::int, %s::int)",
            (lim, offs)
        )
        rows = cur.fetchall()

        if len(rows) == 0:
            print("No contacts.")
        else:
            for row in rows:
                print(row)

        cur.close()
        conn.close()

    def remove_contact(self):
        val = input("Enter name or phone to delete: ")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("CALL delete_contact(%s::text)", (val,))

        conn.commit()
        cur.close()
        conn.close()

        print("Deleted.")

    def menu(self):
        while True:
            print("\nPhoneBook")
            print("1 - Add or update contact")
            print("2 - Add many contacts")
            print("3 - Show all contacts")
            print("4 - Search by pattern")
            print("5 - Show paginated contacts")
            print("6 - Delete by name or phone")
            print("0 - Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.add_many_contacts()
            elif choice == "3":
                self.show_all()
            elif choice == "4":
                self.find_by_pattern()
            elif choice == "5":
                self.show_paginated()
            elif choice == "6":
                self.remove_contact()
            elif choice == "0":
                break
            else:
                print("Wrong choice")


app = PhoneBook()
app.menu()