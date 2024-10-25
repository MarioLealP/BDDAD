SELECT 
    c.Name AS CustomerName,
    p.Name AS ProductName,
    po.Quantity,
    co.DeliveryDate
FROM 
    CostumerOrder co
INNER JOIN 
    ProductOrder po ON co.ID = po.OrderID
INNER JOIN 
    Costumer c ON co.CostumerID = c.ID
INNER JOIN 
    Product p ON po.ProductCode = p.Code
WHERE 
    co.DeliveryDate BETWEEN TO_DATE('2024-09-22', 'YYYY-MM-DD') AND TO_DATE('2024-09-30', 'YYYY-MM-DD')
ORDER BY 
    co.DeliveryDate;
