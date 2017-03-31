def batalha(p,v,d,pp,vp,dp):
	while vp > 0 and v > 0:
		v=v-(pp-d)
		if v<=0:
			return v=0
		vp=vp-(p-dp)
		if vp<=0:
			return vp=0