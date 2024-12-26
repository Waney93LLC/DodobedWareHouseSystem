from django.db import models

from account.models import Address, User


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_information = models.ForeignKey(Address,on_delete=models.CASCADE)   
    priority_level = models.Choices(
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )

    def __str__(self):
        return self.customer_id


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    definition_document = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    definition_document = models.URLField(max_length=200)
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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=100)
    order_date = models.DateField()
    delivery_deadline = models.DateField()
    priority_level = models.Choices(
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.choiuces(
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )

    def __str__(self):
        return self.order_item_id

# models.Choices(
#         ('Available', 'Available'),
#         ('On Hold', 'On Hold'),
#         ('Damaged', 'Damaged'),
#         ('Reserved', 'Reserved'),
#         ('Out of Stock', 'Out of Stock'),
#         ('Back Ordered', 'Back Ordered'),
#         ()
#     )
class InventoryStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class InventoryLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    building = models.CharField(max_length=100)
    bay = models.CharField(max_length=100)
    aisle = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    available_quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    location = models.ForeignKey(InventoryLocation, on_delete=models.CASCADE)
    status =  models.ForeignKey(InventoryStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.product_name} - {self.location}"


class Workflow(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models. choiuces(
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )
    steps = models.JSONField(default=list)
    created_date = models.DateField()
    completed_date = models.DateField()

    def __str__(self):
        return self.workflow_id

# Assigning tasks can be to a user or a group or a machine
class Workload(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.Choices(
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )
    deadline = models.DateField()

    def __str__(self):
        return self.workload_id

class PlannerEscalation(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    shortage_quantity = models.IntegerField()
    escalation_status = models.Choices(
        ('Good', 'good'),
        ('Warning', 'warning'),
        ('Urgent', 'urgent')
    )
    notified_to = models.CharField(max_length=100) # This can be a group or a user or another system 
    escalation_date = models.DateField()

    def __str__(self):
        return self.escalation_id



class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_information = models.ForeignKey(Address,on_delete=models.CASCADE)
    material_type = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_id

    
class Dashboard(models.Model):
    planner = models.ForeignKey(User, on_delete=models.CASCADE)
    workflow_summary = models.TextField()
    alerts = models.JSONField(default=list)

    def __str__(self):
        return self.dashboard_id

