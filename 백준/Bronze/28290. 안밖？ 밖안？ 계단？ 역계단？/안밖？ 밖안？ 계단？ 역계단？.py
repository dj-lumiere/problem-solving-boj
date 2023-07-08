# 28290 안밖? 밖안? 계단? 역계단?

in_out = ["fdsajkl;", "jkl;fdsa"]
out_in = ["asdf;lkj", ";lkjasdf"]
stair = "asdfjkl;"
reverse_stair = ";lkjfdsa"

keypresses = input()
if keypresses in in_out:
    print("in-out")
elif keypresses in out_in:
    print("out-in")
elif keypresses == stair:
    print("stairs")
elif keypresses == reverse_stair:
    print("reverse")
else:
    print("molu")