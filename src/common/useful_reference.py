import os, sys

# **************************"
# os env settings"
# **************************"
for a in os.environ:
    print('Var: ', a, 'Value: ', os.getenv(a))

# **************************"
# python version
# **************************"
print("Python version => {0} ".format(sys.version_info))

# **************************"
# useful sys settings
# **************************"
print(sys.stdout.encoding)
print(sys.stdout.isatty())
print(os.environ["PYTHONIOENCODING"])

# **************************"
# misc useful settings
# **************************"
print(chr(246), chr(9786), chr(9787))
