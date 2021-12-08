# Global constants
screen_size = "800x870"

x_path = "img/x.png"
check_path = "img/check.png"
x_and_check_size = (15, 15)

EC_LIST = {
    "secp192r1": {
        "q": 0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        "a": 0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        "b": 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
        "g": (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012,
              0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811),
        "n": 0xffffffffffffffffffffffff99def836146bc9b1b4d22831,
        "h": 0x1
    },
    "secp224r1": {
        "q": 0xffffffffffffffffffffffffffffffff000000000000000000000001,
        "a": 0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe,
        "b": 0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4,
        "g": (0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21,
              0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34),
        "n": 0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d,
        "h": 0x1
    },
    "secp256r1": {
        "q": 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
        "a": 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc,
        "b": 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
        "g": (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
              0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5),
        "n": 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
        "h": 0x1
    },
    "secp384r1": {
        "q": 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff,
        "a": 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffc,
        "b": 0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef,
        "g": (0xaa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab7,
              0x3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f),
        "n": 0xffffffffffffffffffffffffffffffffffffffffffffffffc7634d81f4372ddf581a0db248b0a77aecec196accc52973,
        "h": 0x1
    },
    "brainpoolP192r1": {
        "q": 0xC302F41D932A36CDA7A3463093D18DB78FCE476DE1A86297,
        "a": 0x6A91174076B1E0E19C39C031FE8685C1CAE040E5C69A28EF,
        "b": 0x469A28EF7C28CCA3DC721D044F4496BCCA7EF4146FBF25C9,
        "g": (0xC0A0647EAAB6A48753B033C56CB0F0900A2F5C4853375FD6,
              0x14B690866ABD5BB88B5F4828C1490002E6773FA2FA299B8F),
        "n": 0xC302F41D932A36CDA7A3462F9E9E916B5BE8F1029AC4ACC1,
        "h": 0x1
    },
    "brainpoolP256r1": {
        "q": 0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377,
        "a": 0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9,
        "b": 0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6,
        "g": (0x8BD2AEB9CB7E57CB2C4B482FFC81B7AFB9DE27E1E3BD23C23A4453BD9ACE3262,
              0x547EF835C3DAC4FD97F8461A14611DC9C27745132DED8E545C1D54C72F046997),
        "n": 0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7,
        "h": 0x1
    }

}


def get_predef_curves_names():
    return list(EC_LIST.keys())


def get_curve(curve_name):
    return EC_LIST[curve_name]
