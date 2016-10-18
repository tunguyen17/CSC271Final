-- A(name, address, title)
-- B(nam, address, salary)
SELECT(CASE
           WHEN a.name IS NOT NULL THEN a.name
           WHEN b.name IS NOT NULL THEN b.name
           ELSE NULL
      END) AS name,
      (CASE
           WHEN a.address IS NOT NULL THEN a.address
           WHEN b.address IS NOT NULL THEN b.address
           ELSE NULL
      END) AS address,
      a.title,
      b.salary,
FROM a FULL OUTER JOIN b ON (a.name = b.name) AND (a.address = b.address);
