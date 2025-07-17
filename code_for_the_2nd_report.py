# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。

def calculate_student_stats(grades):
    """
    一人の学生の成績リストから合計点と平均点を計算する。
    Args:
        grades (list): 成績のリスト (例: [85, 90, 78])
    Returns:
        tuple: (合計点, 平均点)
    """
    total = sum(grades)
    # 成績リストが空の場合にゼロ除算エラーを防ぐ
    if not grades:
        return 0, 0.0
    average = total / len(grades)
    return total, average

def analyze_all_students(students_data):
    """
    全学生のデータを処理し、各学生の統計を表示して、最も成績の良い学生を返す。
    Args:
        students_data (dict): 学生の名前をキー、成績リストを値とする辞書
    Returns:
        tuple: (最も成績の良い学生の名前, その学生の合計点)
    """
    top_student = ""
    max_score = -1  # スコアは0以上と仮定し、確実に最初の学生が選ばれるように-1で初期化

    print("--- Individual Student Scores ---")
    for student_name, grades in students_data.items():
        # 抽出したメソッドを呼び出して、一人の学生の統計を計算
        total, avg = calculate_student_stats(grades)
        print(f"Student: {student_name}, Total: {total}, Average: {avg:.2f}")

        # 最も成績の良い学生を更新
        if total > max_score:
            max_score = total
            top_student = student_name

    return top_student, max_score


# --- メイン実行ブロック ---
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 78],
        "Bob": [92, 88, 84],
        "Charlie": [70, 75, 80],
        "David": [95, 85, 90]
    }

top_student, top_score = run(students)
print("-" * 33)
print(f"Best student: {top_student_name} with total score: {top_total_score}")
