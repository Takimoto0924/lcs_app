# 動的計画法で先頭から1文字ずつ処理
def lcs_length(str1, str2):
    # bを先頭j文字まで限定した場合のLCS長（初期値はaは先頭0文字まで）
    curr_length = [0] * (len(str2) + 1)

    # aを先頭から1文字ずつ追加
    for char1 in str1:
        prev_length = curr_length
        curr_length = [0]

        for j, char2 in enumerate(str2, 1):
            # 一致する文字が存在した場合、bをj-1文字までに限定したときのLCS長+1
            if char1 == char2:
                curr_length.append(prev_length[j - 1] + 1)
            # 一致する文字が存在しない場合、aがi-1文字でbがj文字までのときのLCS長+1 or aがi文字でbがj-1文字までのときのLCS長+1
            else:
                curr_length.append(max(curr_length[-1], prev_length[j]))

    return curr_length[-1]
