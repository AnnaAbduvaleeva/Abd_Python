m = 100
dm = 4
m_left_lst = [m_left for m_left in range(m,-1, -dm)]  # генераторное выражение
print(*m_left_lst)
