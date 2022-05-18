def solution(record):
    answer = []
    dic = {}
    for s in record:
        global command, userId, name
        if len(s.split()) == 3:
            command, userId, name = s.split()
        elif len(s.split()) == 2:
            command, userId = s.split()

        if command == "Enter":
            dic[userId] = name
        elif command == "Change":
            dic[userId] = name

    for s in record:
        if len(s.split()) == 3:
            command, userId, name = s.split()
        elif len(s.split()) == 2:
            command, userId = s.split()

        if command == "Enter":
            answer.append(dic[userId]+"님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(dic[userId]+"님이 나갔습니다.")
    print(answer)
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)