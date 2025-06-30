tasks =[]

def display_menu():
    print('\nタスク管理ツール')
    print('1:タスクを登録')    
    print('2:タスクを表示')
    print('3:タスクを削除')
    print('4:終了')
    
while True:
    display_menu()
    choice = input('操作を選んでください(1～4):')
    
    if choice == '1':
        task = input('登録するタスクを入力してください:')
        tasks.append(task)
        print(f'タスク「{task}」を入力しました。:')
    elif choice =='2':
        if task:
            print('\n登録されているタスク:')
            for i, task in enumerate(task, 1):
                print(f'{i}. {task}')
        else:
            print('タスクがありません')
    
    elif choice =='3':
        if task:
            for i, task in enumerate(task, 1):
                print(f'{i}. {task}')
            try:
                task_num = int(input('削除するタスクの番号を入力してください:'))
                if 1 <=task_num <=len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f'タスク「{removed_task}」を削除しました')
                else:
                    print('無効な番号です')
            except ValueError:
                print('数字を入力してださい')
        elif choice == '4':
            print('プログラムを終了します')
            break
        else:
            print('無効な選択です。1～4を選んでください')
                        
