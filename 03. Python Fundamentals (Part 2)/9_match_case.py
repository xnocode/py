color = input("enter color: ")

match color:
    case "Red":
        print("stop")
    case "Green":
        print("go")
    case "Yellow":
        print("look")
    case _:
        print("wrong color")
        
        