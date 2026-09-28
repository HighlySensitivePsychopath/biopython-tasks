k=int(input())
m=int(input())
n=int(input())

N=k+m+n

m_m=(m/N) * ((m-1)/(N-1))
m_n=(m / N) * (n / (N - 1)) + (n / N) * (m / (N - 1))
n_n=(n/N) * ((n-1)/(N-1))

recessive_probability=m_m*0.25 +m_n*0.5 + n_n


print(1-recessive_probability)

