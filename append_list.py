current_choice = "-"
computer_parts = []
available_items = ["Computer", "monitor", "keyboard", "mouse", "Mouse pad", "HDMI cable"]
valid_choices=[str(i) for i in range(1,len(available_items)+1)]
print(valid_choices)
while current_choice != "0":
    if current_choice in valid_choices:
 #   if current_choice in "123456":
        print(f"Adding {current_choice}")
        index=int(current_choice)-1
        chosen_part=available_items[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append((chosen_part))
        # if current_choice == '1':
        #     computer_parts.append("computer")
        # elif current_choice == '2':
        #     computer_parts.append("monitor")
        # elif current_choice == '3':
        #     computer_parts.append("keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("mouse")
        # elif current_choice == '5':
        #     computer_parts.append("mouse mat")
        # elif current_choice == '6':
        #     computer_parts.append("HDMI cable ")
    else:
        print("please add options from list")

        #         print("1: Computer\n2:monitor\n3: keyboard\n4: mouse\n5: Mouse pad \n6: HDMI cable\n0 to exit")
#        for parts in available_items:
#            print(f"{available_items.index(parts)+1}: {parts}")
        for number,parts in enumerate(available_items):
            print(f"{number+1}: {parts}")
    current_choice = input()

print(computer_parts)
