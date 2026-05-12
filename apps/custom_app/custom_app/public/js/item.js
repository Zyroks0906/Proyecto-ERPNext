frappe.ui.form.on('Item', {
    validate: function(frm) {
        // Tarea A de Alejandro: Validación en tiempo real (lado cliente)
        if (frm.doc.custom_warranty_period < 0) {
            frappe.msgprint({
                title: __('Error de Validación'),
                indicator: 'red',
                message: __('El periodo de garantía no puede ser negativo.')
            });
            frappe.validated = false;
        }
        
        if (frm.doc.item_group === 'Hardware' && (frm.doc.custom_warranty_period === 0 || !frm.doc.custom_warranty_period)) {
            frappe.msgprint({
                title: __('Sugerencia de Calidad'),
                indicator: 'orange',
                message: __('Atención: Los productos de tipo <b>Hardware</b> deberían tener un periodo de garantía asignado.')
            });
        }
    }
});
