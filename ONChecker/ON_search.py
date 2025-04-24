import ifcopenshell
import csv
import sys
from collections import defaultdict
from typing import TypedDict, Union, Literal, Optional


class AversioON():  
    def __init__(self):
        self.results={}
        self.results["ifcfilepath"] = ""
        self.results["ifcname"] = ""
        self.results["ifcdescription"] = ""
        self.results["ifctimestamp"] = ""
        self.results["totalchecked"] = ""
        self.results["totalfailed"] = ""
        self.results["failedentities"] = ""
        self.results["failed_percentage"] = ""
    
    def load_keywords_from_csv(self, csv_file):
        keywords = []
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Ensure the row is not empty
                        keywords.append(row[0].strip())
            print(f"[ON info]: Loaded keywords: {keywords}", file=sys.stderr)
            return keywords
        except FileNotFoundError:
            print(f"[ON Error]: CSV file not found: {csv_file}", file=sys.stderr)
            return []
        except Exception as e:
            print(f"[ON Error]: loading keywords: {e}", file=sys.stderr)
            return []

    def load_attributes_from_csv(self, csv_file):
        keywords = []
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Ensure the row is not empty
                        keywords.append(row[0].strip())
            print(f"[ON info]: Loaded attributes: {keywords}", file=sys.stderr)
            return keywords
        except FileNotFoundError:
            print(f"[ON Error]: Attribute file not found: {csv_file}", file=sys.stderr)
            return []
        except Exception as e:
            print(f"[ON Error]: loading attributes: {e}", file=sys.stderr)
            return []

    def search_ifc_for_keywords(self, ifc_file, keywords, attributes):
        """
        Searches the IFC file for keywords and returns a structured list of dictionaries.
        """
        grouped_results = defaultdict(list)
        total_failed_count = 0
        total_checked = 0

        try:
            model = ifcopenshell.open(ifc_file)
            for element in model.by_type("IfcElement"):
                total_checked += 1
                global_id = getattr(element, "GlobalId", None)
                if global_id is None:
                    continue

                for attribute in attributes:
                    attribute_value = getattr(element, attribute, None)
                    for keyword in keywords:
                        if keyword.lower() in str(attribute_value).lower():
                            grouped_results[keyword].append({
                                "GlobalId": global_id,
                                "IfcClass": element.is_a(),
                                "Attribute": attribute,
                                "AttributeValue": attribute_value
                            })
                            total_failed_count += 1
                            break
                    else:
                        for rel in getattr(element, "IsDefinedBy", []):
                            if rel.is_a("IfcRelDefinesByProperties"):
                                property_set = rel.RelatingPropertyDefinition
                                if property_set and property_set.is_a("IfcPropertySet"):
                                    for property in getattr(property_set, "HasProperties", []):
                                        if property.is_a("IfcPropertySingleValue") and getattr(property, "NominalValue", None):
                                            property_value = property.NominalValue.wrappedValue
                                            property_name = property.Name
                                            for keyword in keywords:
                                                if keyword.lower() in str(property_value).lower():
                                                    grouped_results[keyword].append({
                                                        "GlobalId": global_id,
                                                        "IfcClass": element.is_a(),
                                                        "Attribute": property_name,
                                                        "AttributeValue": property_value
                                                    })
                                                    total_failed_count += 1
                                                    break
                                    else:
                                        continue
                                    break

            # Restructure the data for the template
            formatted_results = []
            for keyword, elements in grouped_results.items():
                formatted_results.append({
                    "keyword": keyword,
                    "elements": elements,  # List of elements for this keyword
                    "element_count": len(elements)
                })

            self.results["failedentities"] = formatted_results
            self.results["totalfailed"] = total_failed_count
            self.results["totalchecked"] = total_checked
            
            # Calculate failed percentage
            if total_checked > 0:
                self.results["failed_percentage"] = (total_failed_count / total_checked) * 100
            else:
                self.results["failed_percentage"] = 0

            return formatted_results


        except FileNotFoundError:
            print(f"Error: IFC file not found: {ifc_file}", file=sys.stderr)
            return []
        except Exception as e:
            print(f"Error searching IFC: {e}", file=sys.stderr)
            return []


    def to_file(self, filepath: str, reptemplatepath: str) -> None:
        import pystache
        try:
            with open(reptemplatepath, "r", encoding="utf-8") as file:
                try:
                    rendered_output = pystache.render(file.read(), self.results)
                    with open(filepath, "w", encoding="utf-8") as outfile:
                        outfile.write(rendered_output)
                    print(f"[ON Check Success] Report created successfully in {filepath}", file=sys.stderr)

                except Exception as pystache_error:
                    print(f"[ON Check Error] Pystache rendering failed: {pystache_error}", file=sys.stderr)

        except FileNotFoundError as file_error:
            print(f"[ON Check Error] File operation failed: {file_error}", file=sys.stderr)
        except Exception as general_error:
            print(f"[ON Check Error] An unexpected error occurred: {general_error}", file=sys.stderr)
            
