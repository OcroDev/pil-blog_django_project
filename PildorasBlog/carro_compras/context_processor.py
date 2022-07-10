def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total + ( float( value["precio_precio"] )*value["producto_cantidad"] )
        return {"importe_total_carro":total}
    else:
        return {"importe_total_carro":total}
