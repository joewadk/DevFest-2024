import {
    Box,
    Flex,
    Text,
    HStack,
    useColorModeValue,
    Image,
  } from "@chakra-ui/react";
  import { Link } from "react-router-dom";
  import carbonRouteLogo from "../assets/carbonRouteLogo.png";
  
  export default function Navbar() {
    return (
      <nav>
        <Box bg={useColorModeValue("gray.50", "gray.900")} px={4}>
          <Flex h={16} alignItems={"center"} justifyContent={"space-between"}>
            <Link to="/">
              <Box>
                <HStack spacing={8} alignItems={"center"}>
                  <Text
                    textColor={useColorModeValue("blue.500", "blue.400")}
                    fontWeight={"bold"}
                    display={"flex"}
                    alignItems={"center"}
                  >
                    <Image src={carbonRouteLogo} width={8} margin={"5px"} />
                    Carbon Route
                  </Text>
                </HStack>
              </Box>
            </Link>
          </Flex>
        </Box>
      </nav>
    );
  }
  