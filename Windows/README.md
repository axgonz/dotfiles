# Windows config files

## Glaze Window Manager

Copy `.glzr` to `%USERPROFILE%\`

## Power Run (PowerToys)

Copy `AppData` to `%USERPROFILE%\`

## Remaps

Run `remaps.reg`

### Key codes

```
CAPS= 3a,00
LCTL= 1d,00

INST= 52,00
NUML= 45,00

LALT= 38,00
LWIN= 5b,e0

PGUP= 49,00
PGDN= 51,00
LEFT= 4b,00
RIHT= 4d,00
```

### Remaps

```
# LCTL <- CAPS
1d,00,3a,00,

# LALT <- LWIN
38,00,5b,e0,

# NULL <- Insert
00,00,52,e0,

# Left <- PgUp
4b,00,49,00,

# Right <- PgDn
4d,00,51,00,
```

```
00,00,00,00,00,00,00,00,
06,00,00,00,1d,00,3a,00,
38,00,5b,e0,00,00,52,e0,
00,00,49,e0,00,00,51,e0,
00,00,00,00
```

### Example

```
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]

"Scancode Map"=hex:00,00,00,00,00,00,00,00,04,00,00,00,53,e0,37,e0,1d,e0,5c,e0,37,e0,52,e0,00,00,00,00

# Header
00,00,00,00,00,00,00,00,

# Number of remaps
04,

# Padding
00,00,00,

# 1st remap
53,e0,37,e0,

# 2nd remap
1d,e0,5c,e0,

# 3rd remap
37,e0,52,e0,

# 4th remap (a required Null remap)
00,00,00,00%
```

