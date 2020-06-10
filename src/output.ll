declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strps = constant [4 x i8] c"%s\0A\00"
@strsi = constant [3 x i8] c"%d\00"
@strsd = constant [4 x i8] c"%lf\00"

["define main @ 'main' () nounwind {", '\n', '  ', "define main @ 'main' () nounwind {", '\n', '  ', 'ret void', '\n', '  ', '', '\n', '}', '\n', '\n']define i32 @main() nounwind {
['  ', '', '\n']  ret i32 0
}
