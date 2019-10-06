def leadinghand(h,m):
  h=(h%12)*5
  if h > m:
    return ("hour hand")
  elif h < m:
    return ("minute hand")
  else:
    return ("draw")