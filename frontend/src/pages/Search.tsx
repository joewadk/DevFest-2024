import Navbar from "../components/Navbar";
import {
  Box,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  Stack,
  Flex,
  Button,
  useColorModeValue,
  ScaleFade,
  Heading,
  Text,
} from "@chakra-ui/react";
import { useState } from "react";

export default function Search() {
  const [carbonFootprint, setCarbonFootprint] = useState(null);
  const [carbonForm, setCarbonForm] = useState({
    user_address: "",
    source_address: "",
    package_weight: "",
  });
  const [isLoading, setIsLoading] = useState(false);

  async function handleOnSubmit() {
    setIsLoading(true);

    const requestUrl = "http://127.0.0.1:5000/carbon_emission";
    const requestInit = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(carbonForm),
    };
    const response = await fetch(requestUrl, requestInit);
    const responseData = await response.json();
    setCarbonFootprint(responseData.carbon);

    setIsLoading(false);
  }

  function resetForm() {
    setCarbonFootprint(null);
    setCarbonForm({
      user_address: "",
      source_address: "",
      package_weight: "",
    });
  }

  function handleInputChange(event) {
    // remove error message
    const fieldName = event.target.name;
    const fieldValue = event.target.value;
    setCarbonForm({
      ...carbonForm,
      [fieldName]: fieldValue,
    });
  }

  return (
    <>
      <Navbar />
      <Flex
        justify={"center"}
        direction={"column"}
        alignItems={"center"}
        bg={useColorModeValue("gray.50", "gray.800")}
        h={"95vh"}
      >
        {!carbonFootprint ? (
          <>
            <Stack
              spacing={8}
              mx={"auto"}
              w={"full"}
              maxW={"700px"}
              py={12}
              px={6}
            >
              <Stack align={"center"}>
                <Heading fontSize={"4xl"}>Welcome!</Heading>
                <Text fontSize={"lg"} color={"gray.600"}>
                  Find Your Carbon Footprint
                </Text>
              </Stack>
            </Stack>
            <ScaleFade initialScale={0.9} in={true}>
              <Box
                w={"700px"}
                rounded={"lg"}
                bg={useColorModeValue("white", "gray.700")}
                boxShadow={"lg"}
                p={8}
                alignSelf={"center"}
              >
                {/* {errorMsg && (
            <Alert status="error" variant={"subtle"} mb={"10px"}>
                <AlertIcon />
                <AlertDescription>{errorMsg}</AlertDescription>
            </Alert>
            )} */}
                <Stack spacing={4}>
                  <FormControl id="user_address">
                    <FormLabel>Your Address</FormLabel>
                    <Input
                      name="user_address"
                      value={carbonForm.user_address}
                      onChange={handleInputChange}
                    />
                  </FormControl>
                  <FormControl id="source_address">
                    <FormLabel>Source Address</FormLabel>
                    <Input
                      name="source_address"
                      value={carbonForm.source_address}
                      onChange={handleInputChange}
                    />
                  </FormControl>
                  <FormControl id="package_weight" isRequired>
                    <FormLabel>Package Weight (in pounds)</FormLabel>
                    <InputGroup>
                      <Input
                        type={"number"}
                        name="package_weight"
                        value={carbonForm.package_weight}
                        onChange={handleInputChange}
                      />
                    </InputGroup>
                  </FormControl>

                  <Stack>
                    <Stack
                      direction={{ base: "column", sm: "row" }}
                      align={"start"}
                      justify={"space-between"}
                    ></Stack>
                    <Button
                      onClick={handleOnSubmit}
                      isLoading={isLoading}
                      bg={"blue.400"}
                      color={"white"}
                      _hover={{
                        bg: "blue.500",
                      }}
                    >
                      Calculate
                    </Button>
                  </Stack>
                </Stack>
              </Box>
            </ScaleFade>
          </>
        ) : (
          <>
            <Stack
              spacing={8}
              mx={"auto"}
              w={"full"}
              maxW={"700px"}
              py={12}
              px={6}
            >
              <Stack align={"center"} spacing={"20px"}>
                {/* <Heading fontSize={"4xl"}>Welcome!</Heading> */}
                <Text fontSize={"x-large"} color={"gray.600"}>
                  The carbon footprint of this package is{" "}
                  <strong>{carbonFootprint * 1000}</strong> pounds
                </Text>
                <Button
                  onClick={resetForm}
                  isLoading={isLoading}
                  bg={"blue.400"}
                  color={"white"}
                  size={"lg"}
                  _hover={{
                    bg: "blue.500",
                  }}
                >
                  Calculate Another Shipment
                </Button>
              </Stack>
            </Stack>
          </>
        )}
      </Flex>
    </>
  );
}
