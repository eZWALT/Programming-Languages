
fact1::Integer->Integer
fact1 0 = 1
fact n = n * (fact (n-1))

fact2::Integer->Integer
fact2 n  = product([x | x<-[1..n]])

fact3::Integer->Integer
fact3 n = foldl (*) 1 [1..n]

fact4::Integer->Integer
fact4 n = head(scanr (*) 1 [1..n])
