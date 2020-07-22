li = [['祝', '大', '家'], 
      ['学', '习', '好'], 
      ['身', '体', '棒']]

print('\n'.join(' '.join(i) for i in li) + '\n')
print('\n'.join(' '.join(i) for i in [[li[j][k] 
    for j in range(len(li))] 
    for k in range(len(li[0]))]))

# 来波炫技
print('\n'.join(' '.join(i) for i in zip(*li)))
