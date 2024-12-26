from django.db import models

from account.models import Address, User

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductLine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    product_internal_name = models.CharField(max_length=100)
    drawing_url = models.URLField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    material_type = models.ForeignKey(Material, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    weight_unit_of_measure = models.ForeignKey(Unit, on_delete=models.CASCADE)
    productline = models.ForeignKey(ProductLine, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=100)
    order_date = models.DateField()
    delivery_deadline = models.DateField()
    priority_level = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.order_item_id

class Inventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    available_quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.inventory_id

class Workflow(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_date = models.DateField()
    completed_date = models.DateField()

    def __str__(self):
        return self.workflow_id

class Workload(models.Model):
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.CharField(max_length=100)
    deadline = models.DateField()

    def __str__(self):
        return self.workload_id

class PlannerEscalation(models.Model):
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    shortage_quantity = models.IntegerField()
    escalation_status = models.CharField(max_length=100)
    notified_to = models.CharField(max_length=100)
    escalation_date = models.DateField()

    def __str__(self):
        return self.escalation_id

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_information = models.ForeignKey(Address,on_delete=models.CASCADE)   
    priority_level = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_id



class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_information = models.TextField()
    material_type = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_id

    
class Dashboard(models.Model):
    planner = models.ForeignKey(User, on_delete=models.CASCADE)
    workflow_summary = models.TextField()
    inventory_status = models.TextField()
    alerts = models.JSONField(default=list)

    def __str__(self):
        return self.dashboard_id

