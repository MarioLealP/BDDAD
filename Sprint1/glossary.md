**Product:** is an item manufactured at the factory, it has a **BoM** and a **BoO**, **components** and **raw resources** are also **products**.

**Components:** are intermidiary steps in the production of a **Product**

**Raw Resources:** are the basic materials required to assemble and **Product**

**Bill of Materials (BoM):** lists all the materials required to manufacture a product

**Stations:** are either a robot unit, automated machine, machine operated by an Human or a Human workstation it has an **Operation** it performs

**Bill of Operations (BoO):** lists the **operations** and step required to manufacture a **product**

**Operation:** a task required to be executed on a **product**

**Production Plan:** compiles the **Production Orders** into a plan with a specific time

**Production Orders:** lists a certain **Product** in addition it's size and color

**Costumer Order:** has a unique ID, a costumer ID, a list of **Production Order** and a delivery **date** and **address**

**Costumer:** has a **NIF**, **name**, **address**, **contact** and **Costumer Type**

**NIF**: 8 number code

**Name:** at least 2 strings

**Contact:** 9 number code

**Address**: Composed by a street name, door number and postcode (can be duplicated so needs an ID)

**Type:** Individual or Company

**System User**: Has a role **Production Manager**, **Plant Floor Manager**, **Administrator**

**Production Manager**: maintains information related to **products** and used raw materials also controls information associated with **production orders**

**Plant Floor Manager:** specifies factory
